import json
import datetime
import http.client
from time import time

conn = http.client.HTTPConnection("localhost:5030") 
#conn_mongo = http.client.HTTPConnection("localhost:5020")

headers = {
    'Content-type': 'application/json'
}

url = "/users/create"

login_data = {
    'username': 'blue',
    'password': '123456'
}

create_data = {
    'email': 'lazar@gmail.com',
    'name': 'Lazarbeam',
    'password': '123456',
    'username': 'lazar'
}

def slashOnly(url):
    copy = url.split('/')
    copy.pop(0)
    return copy

def interrogation(url):
    copy = url.split('/')
    copy[1] = copy[1].split('?')
    copy = copy[1]
    return copy

def gateway(url, login_data):
    if '?' in url:
        copy = interrogation(url)
    else:
        copy = slashOnly(url)
    print(copy)
    json_data_post = json.dumps(login_data)
    #print(json_data_post)

    if copy[0] == 'persons':
        conn_neo4j = http.client.HTTPConnection("localhost:5000")
        if len(copy) == 1 or copy[2] in ['delete', 'person1']:
            conn_neo4j.request('POST', url, headers=headers)
        else:
            conn_neo4j.request('GET', url, headers=headers)
        
        res = conn_neo4j.getresponse()
        data = res.read()
        print(data.decode("utf-8"))

    elif copy[0] == 'users':

        conn_mysql = http.client.HTTPConnection("localhost:5010")
        print(json_data_post)

        if copy[1] != 'create':

            conn_mysql.request("POST", "/users/login", json_data_post, headers=headers)
            res = conn_mysql.getresponse()
            data = res.read()

            data_json = json.loads(data.decode("utf-8"))
            print(data_json)
            jwt_token = data_json['token']

            new_headers = {
                'Content-type': 'application/json',
                'authorization': jwt_token
            }

            if len(copy) > 4:
                conn_mysql.request('POST', url, headers=new_headers)
            else:
                conn_mysql.request('GET', url, headers=new_headers)

        else:
            #print("Hola wapo")
            conn_mysql.request("POST", url, json_data_post, headers=headers)

        res = conn_mysql.getresponse()
        data = res.read()
        print(data.decode("utf-8"))  

gateway(url, create_data)
