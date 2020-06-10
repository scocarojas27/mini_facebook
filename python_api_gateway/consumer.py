import json
import datetime
import http.client
from time import time

conn = http.client.HTTPConnection("localhost:5030") 
#conn_mongo = http.client.HTTPConnection("localhost:5020")

headers = {
    'Content-type': 'application/json'
}

url = "/gateway/users/create"

login_data = {
    'username': 'blue',
    'password': '123456'
}

create_data = {
    'email': 'fresh@gmail.com',
    'name': 'Mr Fresh',
    'password': '123456',
    'username': 'fresh'
}
json_data_post = json.dumps(create_data)
conn.request("GET", url, json_data_post, headers=headers)
