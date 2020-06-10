from flask import Blueprint
import db_config
from flask import jsonify, request
from flask_jwt_extended import (
    jwt_required, fresh_jwt_required, JWTManager, jwt_refresh_token_required,
    jwt_optional, create_access_token, create_refresh_token, get_jwt_identity,
    decode_token
)
from services.PublicationsService import PublicationsService
from app import app

publications_api = Blueprint('publications_api', __name__)

publications_service = PublicationsService()

@publications_api.route('/publications',
                        methods = ['POST'])
@jwt_required
def create_publication():
    try:
        app.logger.info("in /publications[POST]")
        publication_body = request.json
        #print(publication_body)
        if 'user_id' in publication_body and 'description' in publication_body:
            print("Hola")
            app.logger.info("user_id: " + str(publication_body['user_id']) + ' - description: ' + str(publication_body['description']))
            result = publications_service.send_publication(publication_body)
            print("Hola 3")
            if result:
                resp = jsonify({'message': 'publication received'})
                resp.status_code = 201
            else:
                resp = jsonify({'message': 'publication was not received'})
                resp.status_code = 500
        else:
            resp = jsonify({'message': 'the server was unable to process the request sent by the client due to invalid message syntax'})
            resp.status_code = 400
        return resp
    except Exception as e:
        resp = jsonify({'message': 'unknown error'})
        resp.status_code = 500
        return resp

@publications_api.route('/ping',
                        methods = ['GET'])
def ping():
    try:
        app.logger.info("in /ping")
        count = publications_service.documents_count()
        if count >= 0:
            resp = jsonify({'message': 'pong'})
            resp.status_code = 200
        else:
            resp = jsonify({'message': 'error'})
            resp.status_code = 500
    except Exception as e:
        app.logger.error(str(e))
        resp = jsonify({'message': 'error'})
        resp.status_code = 500
    return resp

@publications_api.route('/publications',
                        methods = ['GET'])
@jwt_required
def get_own_publications():
    try:
        app.logger.info("in /publications[GET]")
        publication_body = request.json
        if "user_id" in publication_body:
            posts = publications_service.get_own_posts(publication_body["user_id"])
            resp = jsonify({"message" : "publications", "data" : posts})
            resp.status_code=200
        else:
            resp = jsonify({'message': 'the server was unable to process the request sent by the client due to invalid message syntax'})
            resp.status_code = 400
        return resp
    except Exception as e:
        app.logger.error(str(e))
        resp = jsonify({'message': 'error'})
        resp.status_code = 500

@publications_api.route('/publications/friends',
                        methods = ['GET'])
@jwt_required
def get_friends_publications():
    try:
        app.logger.info("in /publications/friends[GET]")
        publication_body = request.json
        if "user_id" in publication_body:
            posts = publications_service.get_friends_posts(publication_body["user_id"])
            resp = jsonify({"message" : "friends publications", "data" : posts})
            resp.status_code=200
        else:
            resp = jsonify({'message': 'the server was unable to process the request sent by the client due to invalid message syntax'})
            resp.status_code = 400
        return resp
    except Exception as e:
        app.logger.error(str(e))
        resp = jsonify({'message': 'error'})
        resp.status_code = 500