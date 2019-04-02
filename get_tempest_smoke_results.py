#!/usr/bin/python3

# Script fetches tempest smoke results from mosci and dumps to 2 json files

import urllib.request, json , os, time, keyboard, sys, re
import time
import copy

os.environ['http_proxy'] = ''

numBuilds = 100
smokeUrl = "http://mosci:8080/view/3.%20Openstack%20Tests/job/pipeline%20test%20-%20openstack%20-%20tempest%20smoke"

count = 1 
sleeptime = 5
matrix = {}
matrix_full = {}
matrix_last = {}
addrow = False
with urllib.request.urlopen(smokeUrl+ "/api/json/") as url:
    data = json.loads(url.read().decode())
    #fakedata = [150, 140, 127, 137, 122]
    for build in data['builds'][:numBuilds]:
    #for build in fakedata:
        buildId = build['number']
        #buildId = build
        #if count % 2 == 0:
        #    INV = bcolors.INV_ON
        #else:
        count += 1
        lastline = ""
        with urllib.request.urlopen("{}/{}/api/json".format(smokeUrl,buildId)) as jsonurl:
            jsdata = json.loads(jsonurl.read().decode())
            datetime = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(jsdata['timestamp'] / 1000))
        with urllib.request.urlopen("{}/{}/wfapi/describe".format(smokeUrl,buildId)) as wfapiurl:
            wfdata = json.loads(wfapiurl.read().decode())
            #print(wfdata['status'])
            buildnum = "[ {} ]".format(wfdata['id'])
            #print(buildnum)
            failurl = "{}/{}/consoleFull".format(smokeUrl,buildId)
            #print(failurl)
            details = ""
            with urllib.request.urlopen(failurl) as consoleOut:
                console_data = consoleOut.read().decode("utf-8")
                capture = False
                tempest_result = ""
                for line in console_data.split('\n'):
                    if "bundle_url" in line.lower():
                        details = line
                    if 'output below' in line.lower():
                        capture = True
                    if  'worker balance' in line.lower():
                        capture = False
                    if capture == True:
                        if lastline == "":
                            lastline = line
                        #print(lastline)
                        if '------' in line:
                            tempest_result = tempest_result + lastline + "\n"
                        else:
                            lastline = line
                #detcount = 0 
                #for item in details.split('/'):
                #    print("detail {}: {}".format(detcount, item))
                #    detcount += 1
                if details != "":
                    arch = details.split('/')[4].split()[4]
                    bundleType= '-'.join(details.split('/')[12].split('-')[0:2])
                    ubuntuRelease = details.split('/')[12].split('-')[2]
                    openstackRelease = details.split('/')[12].split('-')[3]
                    if tempest_result == "":
                        tempest_result = "SUCCESS"
                    #print("datetime:{},"\
                    #      " arch: {},"\
                    #      " type: {},"\
                    #      " ubuntu release: {},"\
                    #      " openstack release: {}"\
                    #      .format(datetime, arch,
                    #             bundleType,
                    #             ubuntuRelease,
                    #             openstackRelease)
                    #)
                    matrix = {buildId: {
                              'timestamp': datetime,
                              'arch': arch,
                              'type': bundleType,
                              'ubuntu release': ubuntuRelease,
                              'openstack release': openstackRelease,
                              'tempest result': tempest_result
                              }}
                #print("Updating: {}".format(matrix))
                # 1. build matrix dict
                # check if its already in the full one - if it is, skip
                # if its not, add it
                    matrix_full.update(matrix)
                    if matrix_last == {}:
                        matrix_last.update(matrix)
                    else:
                        temp_matrix = copy.deepcopy(matrix)
                        del temp_matrix[buildId]['tempest result']
                        del temp_matrix[buildId]['timestamp']
                        counter = 0 
                        #print (len(matrix_last.items()))
                        #for k, v in matrix_last.items():
                            #print("Key: {}\nValue: {}".format(k, v))
                        for k, row in matrix_last.items():
                            #print("length of matrix_last.items: {}".format(len(matrix_last)))
                            #print("row counter: {}".format(counter))
                            counter += 1
                            rrow = copy.deepcopy(row)
                            #print("ALL THINGS: {}".format(rrow))
                            del rrow['timestamp']
                            del rrow['tempest result']
                            #print(type(rows[0]))
                            #print("compare: \n{}\n{}\n".format(temp_matrix[buildId],rrow))
                            if temp_matrix[buildId] == rrow:
                            #if temp_matrix[buildId] in matrix_last.items():
                            #if row in matrix_last:
                                #print("FOUND existing, not adding: {}".format(matrix[buildId]))
                                addrow = False
                                break
                            else:
                                #print("not found, adding")
                                addrow = True
                    if addrow == True:
                        matrix_last.update(matrix)
    with open('results_full.json', 'w') as outfile:
    	json.dump(matrix_full, outfile)
    with open('results_last.json', 'w') as outfile:
    	json.dump(matrix_last, outfile)
