import json
import datetime
import http.client
from time import time

########################################################################################################################
##################################################### ENVIRONMENTS #####################################################
########################################################################################################################

# connection to publications api service
conn = http.client.HTTPConnection("localhost:5020")
#conn = http.client.HTTPConnection("localhost:8282")


########################################################################################################################
######################################################## LOGIN #########################################################
########################################################################################################################

def login():
    # connection to users api service
    conn_login = http.client.HTTPConnection("localhost:5010")
    headers_default = {'Content-type': 'application/json'}

    login_post = {
        'username': 'white',
        'password': 'qwerty'
    }
    json_data_post = json.dumps(login_post)
    conn_login.request("POST", "/users/login", json_data_post, headers=headers_default)

    res = conn_login.getresponse()
    data = res.read()

    data_json = json.loads(data.decode("utf-8"))
    # print(data_json)
    jwt_token = data_json['token']

    headers = {
        'Content-type': 'application/json',
        'authorization': jwt_token
    }

    return headers

###############
#### LOGIN ####
###############
headers = login()
# print(headers)
# headers={'Content-type': 'application/json'}

login_post = {
    'user_id': 2,
    'description': 'Hola qué más'
}
query_post = {
    'user_id' : 1
}
data_get = json.dumps(query_post)
json_data_post = json.dumps(login_post)
conn.request("POST", "/publications", json_data_post, headers=headers) #Creación de una publicación
#conn.request("GET", "/publications/mypubs", data_get, headers=headers) #Consulta las publicaciones de un usuario
#conn.request("GET", "/publications/friends", data_get, headers=headers) #consulta las publicaciones de los amigos de un usuario

# conn.request("GET", "/ping", headers={'Content-type': 'application/json'})

start = datetime.datetime.now()
res = conn.getresponse()
end = datetime.datetime.now()

data = res.read()

elapsed = end - start

print(data.decode("utf-8"))
print("\"" + str(res.status) + "\"")
print("\"" + str(res.reason) + "\"")
print("\"elapsed seconds: " + str(elapsed) + "\"")

