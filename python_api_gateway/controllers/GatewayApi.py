from flask import Blueprint, request
from app import app
from services.GatewayService import GatewayService
from flask import jsonify
from bson import json_util, ObjectId
import json
gateway_api = Blueprint('gateway_api', __name__)

gateway_service = GatewayService()

@gateway_api.route('/gateway/', methods=['GET'])
def gateway(data, url):
    new_url = url[8:]
    print(url)
    print(new_url)
    try:
        gateway_service.gateway(data, new_url)
        print("Hola")
    except Exception as e:
        print(e)