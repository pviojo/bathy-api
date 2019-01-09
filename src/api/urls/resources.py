import json
import copy

from flask import request, abort

from main import app

from resources.services import ResourceService

@app.route("/resource/<id>/status/<status>", methods=['PUT'])
def change_resource_status(id, status):
    resource = ResourceService.set_status(id, status)
    if not resource:
        abort(404)
    
    return (resource.json(), 200) 

@app.route("/resource/<id>", methods=['GET'])
def get_resource(id):
    resource = ResourceService.get(id)
    if not resource:
        abort(404)
    
    return (resource.json(), 200) 





@app.route("/resources", methods=['GET'])
def get_all():
    resources = ResourceService.all()
    if not resources:
        abort(404)
    
    return ([resource.json() for resource in resources], 200) 



