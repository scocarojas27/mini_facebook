from flask import Blueprint, request
from app import app
from services.GatewayService import GatewayService
from flask import jsonify
from bson import json_util, ObjectId
import json
gateway_api = Blueprint('gateway_api', __name__)

gateway_service = GatewayService()

@gateway_api.route('/gateway/', methods=['GET', 'POST'])
def gateway(url):
    new_url = url[8:]
    try:
        gateway_service.gatewaynew_url)
    except Exception as e:
        print(e)