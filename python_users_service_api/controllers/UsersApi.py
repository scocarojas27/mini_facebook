from flask import Blueprint
from flask import jsonify, request
from flask_jwt_extended import (
    jwt_required, fresh_jwt_required, JWTManager, jwt_refresh_token_required,
    jwt_optional, create_access_token, create_refresh_token, get_jwt_identity,
    decode_token
)
from services.UsersService import UsersService
from app import app

users_api = Blueprint('users_api', __name__)

users_service = UsersService()

@users_api.route('/users/create',
                 methods = ['POST'])

def create_new_user():
    #Recibe la petición de creación de usuario y la envía al repository para crearlo
    try:
        app.logger.info("in /users")
        json = request.json
        email = json['email']
        name = json['name']
        password = json['password']
        username = json['username']
        #print("Este es el: "+str(username))
        if email is not None and name is not None and password is not None and username is not None:
            user = users_service.create_new_user(email, name, password, username)
            if user is None:
                resp = jsonify({'message': 'username or email already exists'})
                resp.status_code = 402
            else:
                resp = jsonify(user)
                resp.status_code = 200
        else:
            resp = jsonify({'message': 'invalid or missing input'})
            resp.status_code = 403
        return resp
    except Exception as e:
        print(e)

@users_api.route('/users/login',
                 methods = ['POST'])
def login():
    #Valida las credenciales del usuario y devuelve un token de seguridad que lo certifica
    try:
        app.logger.info("in /login")
        json = request.json
        username = json['username']
        password = json['password']
        user_id = users_service.login(username,
                                      password)
        app.logger.info("user_id: " + str(user_id['id']))
        #print(user_id)
        #print(username)
        #print(password)
        if user_id is None:
            resp = jsonify({'message': 'incorrect username or password'})
            resp.status_code = 401
        else:
            access_token = create_access_token(identity=user_id['id'])
            resp = jsonify({'token': 'Bearer {}'.format(access_token)})
            resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

@users_api.route('/users',
                 methods = ['GET'])
@jwt_required
def get_users():
    #Recibe las peticiones de búsqueda de usuarios, ya sea por id o nombre
    try:
        app.logger.info("in /users")
        user_id = request.args.get('id', default = None, type = int)
        user_name = request.args.get('name', default = None, type = str)
        if user_id is not None:
            user = users_service.get_user_by_id(user_id)
            app.logger.info("user: " + str(user)+" este es el nombre" +str(user['name']))
            if user is None:
                resp = jsonify({'message': 'user not found'})
                resp.status_code = 404
            else:
                resp = jsonify(user)
                resp.status_code = 200
        elif user_name is not None:
            app.logger.info("Este es el nombre "+str(user_name))
            user = users_service.get_user_by_name(user_name)
            app.logger.info("user: " + str(user))
            if user is None:
                resp = jsonify({'message': 'user not found'})
                resp.status_code = 404
            else:
                resp = jsonify(user)
                resp.status_code = 200
        else:
            # Buscar todos los usuarios
            users = users_service.get_all_users()
            resp = jsonify(users)
            resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

@users_api.route('/users/user1/<int:userId1>/user2/<int:userId2>/send-friend-request',
                 methods = ['POST'])
@jwt_required
def send_friend_request(userId1, userId2):
    #Recibe las solicitudes de amistad y las direcciona al repository para que sean creadas
    try:
        app.logger.info("in /users")
        if userId1 is not None and userId2 is not None:
            friend_request = users_service.send_friend_request(userId1, userId2)
            app.logger.info("user: " + str(userId1) + "sent a friend request to user: " + str(userId2))
            if friend_request is None:
                resp = jsonify({'message': 'user(s) not found'})
                resp.status_code = 404
            else:
                resp = jsonify(friend_request)
                resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

@users_api.route('/users/<int:userId>/friend-requests',
                 methods = ['GET'])
@jwt_required
def friend_requests():
    #Recibe la petición de consulta de solicitudes de amistad de una persona
    try:
        app.logger.info("in /users")
        user_id = request.args.get('userId', default = None, type = int)
        if user_id is not None:
            friend_requests = users_service.friend_requests(user_id)
            app.logger.info("user's " + str(user_id) + "friend requests: ")
            if friend_requests is None:
                resp = jsonify({'message': 'user does not have any friend request'})
                resp.status_code = 404
            else:
                resp = jsonify(friend_requests)
                resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

@users_api.route('/users/<int:userId>/friendRequestId/<int:friendRequestId>/status/<string:status>',
                 methods = ['POST'])
@jwt_required
def respond_friend_request(userId, friendRequestId, status):
    #Recibe la petición de modificar el estado de una solicitud de amistad
    try:
        app.logger.info("in /users")
        states = ['accepted', 'rejected']
        if userId is not None and friendRequestId is not None and status is not None and status in states:
            friend_request = users_service.respond_friend_request(userId, friendRequestId, status)
            app.logger.info("friend requests: " + str(status))
            if friend_requests is None:
                resp = jsonify({'message': 'request does not exists'})
                resp.status_code = 404
            else:
                resp = jsonify(friend_request)
                resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

@users_api.route('/ping',
                 methods = ['GET'])
def ping():
    try:
        app.logger.info("in /ping")
        count = users_service.users_count()
        if count > 1:
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