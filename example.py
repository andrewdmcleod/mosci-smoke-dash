import json
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ugf uyfyitdy fougiuf iytfciygvc iygcycyi'
# app.debug = env['app.debug']

DATA = {'140': {'arch': 'amd64', 'type': 'openstack-telemetry', 'ubuntu release': 'xenial', 'openstack release': 'queens', 'tempest result': 'setUpClass (tempest.api.compute.servers.test_create_server.ServersTestBootFromVolume)\ntempest.api.volume.test_volumes_get.VolumesGetTest.test_volume_create_get_update_delete_from_image[id-54a01030-c7fc-447c-86ee-c1182beae638,image,smoke]\n'}, '139': {'arch': 'amd64', 'type': 'openstack-base', 'ubuntu release': 'xenial', 'openstack release': 'ocata', 'tempest result': 'setUpClass (tempest.api.compute.servers.test_create_server.ServersTestBootFromVolume)\nsetUpClass (tempest.api.object_storage.test_account_services.AccountTest)\nsetUpClass (tempest.api.object_storage.test_container_services.ContainerTest)\nsetUpClass (tempest.api.object_storage.test_account_quotas.AccountQuotasTest)\nsetUpClass (tempest.api.object_storage.test_container_quotas.ContainerQuotasTest)\nsetUpClass (tempest.api.object_storage.test_object_services.ObjectTest)\ntempest.api.volume.test_volumes_get.VolumesGetTest.test_volume_create_get_update_delete_from_image[id-54a01030-c7fc-447c-86ee-c1182beae638,image,smoke]\n'}, '138': {'arch': 'ARMv5', 'type': 'openstack-base', 'ubuntu release': 'xenial', 'openstack release': 'ocata', 'tempest result': 'setUpClass (tempest.api.compute.servers.test_create_server.ServersTestBootFromVolume)\nsetUpClass (tempest.api.object_storage.test_account_services.AccountTest)\nsetUpClass (tempest.api.object_storage.test_container_services.ContainerTest)\nsetUpClass (tempest.api.object_storage.test_account_quotas.AccountQuotasTest)\nsetUpClass (tempest.api.object_storage.test_container_quotas.ContainerQuotasTest)\nsetUpClass (tempest.api.object_storage.test_object_services.ObjectTest)\ntempest.api.volume.test_volumes_get.VolumesGetTest.test_volume_create_get_update_delete_from_image[id-54a01030-c7fc-447c-86ee-c1182beae638,image,smoke]\n'}, '137': {'arch': 'ARMv7', 'type': 'openstack-telemetry', 'ubuntu release': 'xenial', 'openstack release': 'queens', 'tempest result': 'setUpClass (tempest.api.compute.servers.test_create_server.ServersTestBootFromVolume)\ntempest.api.volume.test_volumes_get.VolumesGetTest.test_volume_create_get_update_delete_from_image[id-54a01030-c7fc-447c-86ee-c1182beae638,image,smoke]\n'}}


@app.route('/')
def index():
    # for x in data:
    global DATA
    for key, value in DATA.items():
        print(key, value)
    return render_template('index.html', data=DATA)


@app.route('/arch')
def arch():
    # default dict from collections would work here to make it all dynamic
    global DATA
    amd64 = []
    ARMv5 = []
    ARMv7 = []
    for key, value in DATA.items():
        if value['arch'] == 'amd64':
            amd64.append(value)
        elif value['arch'] == 'ARMv5':
            ARMv5.append(value)
        elif value['arch'] == 'ARMv7':
            ARMv7.append(value)
    data = [amd64, ARMv5, ARMv7]
    print(data)
    return render_template('arch.html', data=data)


if __name__ == '__main__':
        app.run()
