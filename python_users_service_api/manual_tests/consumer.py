import json
import datetime
import http.client
from time import time

########################################################################################################################
##################################################### ENVIRONMENTS #####################################################
########################################################################################################################

#local
conn = http.client.HTTPConnection("localhost:5010")

########################################################################################################################
######################################################## LOGIN #########################################################
########################################################################################################################

def login():
    headers_default = {'Content-type': 'application/json'}

    login_post = {
        'username': 'blue',
        'password': '123456'
    }
    json_data_post = json.dumps(login_post)
    conn.request("POST", "/users/login", json_data_post, headers={'Content-type': 'application/json'})

    res = conn.getresponse()
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

create_data = {
    'email': 'red@gmail.com',
    'name': 'Red Head',
    'password': '123456',
    'username': 'redhead'
}
create_data_post = json.dumps(create_data)
#conn.request("GET", "/users?id=2", headers=headers)
#conn.request("POST","/users/user1/1/user2/2/send-friend-request", headers=headers)
#conn.request("POST","/users/2/friendRequestId/4/status/accepted", headers=headers)

# conn.request("GET", "/ping", headers={'Content-type': 'application/json'})

conn.request("POST", "/users/create", create_data_post, headers={'Content-type': 'application/json'})

start = datetime.datetime.now()
res = conn.getresponse()
end = datetime.datetime.now()

data = res.read()

elapsed = end - start

print(data.decode("utf-8"))
print("\"" + str(res.status) + "\"")
print("\"" + str(res.reason) + "\"")
print("\"elapsed seconds: " + str(elapsed) + "\"")

