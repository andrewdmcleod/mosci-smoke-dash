import json
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ugf uyfyitdy fougiuf iytfciygvc iygcycyi'
# app.debug = env['app.debug']

@app.route('/')
def index():
    # for x in data:
    with open('results_last.json') as json_file:
        DATA = json.load(json_file)
    for key, value in DATA.items():
        print(key, value)
    return render_template('index.html', data=DATA)

@app.route('/history')
def index_history():
    # for x in data:
    with open('results_full.json') as json_file:
        DATA = json.load(json_file)
    for key, value in DATA.items():
        print(key, value)
    return render_template('index.html', data=DATA)


@app.route('/arch')
def arch():
    # default dict from collections would work here to make it all dynamic
    global DATA
    amd64 = []
    arm64 = []
    ppc64el = []
    for key, value in DATA.items():
        if value['arch'] == 'amd64':
            amd64.append(value)
        elif value['arch'] == 'arm64':
            arm64.append(value)
        elif value['arch'] == 'ppc64el':
            ppc64el.append(value)
    data = [amd64, arm64, ppc64el]
    print(data)
    return render_template('arch.html', data=data)


if __name__ == '__main__':
        app.run(host='0.0.0.0')
