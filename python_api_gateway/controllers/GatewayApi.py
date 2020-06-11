from flask import Blueprint, request
from app import app
from services.GatewayService import GatewayService
from flask import jsonify
from bson import json_util, ObjectId
import json

gateway_api = Blueprint('gateway_api', __name__)

gateway_service = GatewayService()

@gateway_api.route('/', methods=['GET'], defaults={'path': ''})
@gateway_api.route('/<path:path>', methods=['GET'])

def gateway(path):
    #Recibe el path de la petición y la envia a la función del repositorio
    data = request.json    
    print(path)
    try:
        res = gateway_service.gateway(data, path)
        print("Esta es la: "+str(res))
        if res is None:
            resp = jsonify({'message': 'Bad request'})
            resp.status_code = 402
        else:
            resp = res
        return resp
    except Exception as e:
        print(e)