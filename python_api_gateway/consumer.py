import json
import datetime
import http.client
from time import time

conn = http.client.HTTPConnection("localhost:5030") 

def login(json_data_post):
    conn = http.client.HTTPConnection("localhost:5010")
    conn.request("POST", "/users/login", json_data_post, headers={'Content-type': 'application/json'})
    res = conn.getresponse()
    data = res.read()
    #print(data)
    data_json = json.loads(data.decode("utf-8"))
    jwt_token = data_json['token']

    new_headers = {
        'Content-type': 'application/json',
        'authorization': jwt_token
    }
    return new_headers

headers = {
    'Content-type': 'application/json'
}

url = "/users?id=1"

login_data = {
    'username': 'blue',
    'password': '123456'
}

create_data = {
    'email': 'cosa@gmail.com',
    'name': 'Cosa',
    'password': '123456',
    'username': 'cosa'
}
friend_data = {
    'user_id': 1
}

pub_data = {
    'username': 'blue',
    'password': '123456',
    'user_id' : 1
}

json_data_post = json.dumps(friend_data)
json_data_post_ = json.dumps(pub_data)
new_headers = login(json_data_post_)

#print(new_headers)

#conn.request("GET", url, json_data_post, headers=new_headers)
#conn.request("GET", "/persons/1/friends", json_data_post,headers=headers)
conn.request("GET", "/publications/mypubs", json_data_post_, headers=new_headers)

res = conn.getresponse()
start = datetime.datetime.now()
data = res.read()
end = datetime.datetime.now()
elapsed = end - start

print(data.decode("utf-8"))
print("\"" + str(res.status) + "\"")
print("\"" + str(res.reason) + "\"")
print("\"elapsed seconds: " + str(elapsed) + "\"")
