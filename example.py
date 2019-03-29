import json
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ugf uyfyitdy fougiuf iytfciygvc iygcycyi'
# app.debug = env['app.debug']

data = {"140": {"arch": "amd64", "type": "openstack-telemetry", "ubuntu release": "xenial", "openstack release": "queens", "tempest result": "setUpClass (tempest.api.compute.servers.test_create_server.ServersTestBootFromVolume)\ntempest.api.volume.test_volumes_get.VolumesGetTest.test_volume_create_get_update_delete_from_image[id-54a01030-c7fc-447c-86ee-c1182beae638,image,smoke]\n"}, "139": {"arch": "amd64", "type": "openstack-base", "ubuntu release": "xenial", "openstack release": "ocata", "tempest result": "setUpClass (tempest.api.compute.servers.test_create_server.ServersTestBootFromVolume)\nsetUpClass (tempest.api.object_storage.test_account_services.AccountTest)\nsetUpClass (tempest.api.object_storage.test_container_services.ContainerTest)\nsetUpClass (tempest.api.object_storage.test_account_quotas.AccountQuotasTest)\nsetUpClass (tempest.api.object_storage.test_container_quotas.ContainerQuotasTest)\nsetUpClass (tempest.api.object_storage.test_object_services.ObjectTest)\ntempest.api.volume.test_volumes_get.VolumesGetTest.test_volume_create_get_update_delete_from_image[id-54a01030-c7fc-447c-86ee-c1182beae638,image,smoke]\n"}}


@app.route('/')
def index():
    # for x in data:
    
    return render_template('layout.html', data=data.json())



if __name__ == '__main__':
        app.run()
