import json
import datetime
import http.client
from time import time
#from flask import request

########################################################################################################################
##################################################### ENVIRONMENTS #####################################################
########################################################################################################################

#local
#conn = http.client.HTTPConnection("localhost:8080")

#container
conn = http.client.HTTPConnection("localhost:5000")
print(conn)

########################################################################################################################
######################################################## USERS #########################################################
########################################################################################################################


headers = {
    'Content-type': 'application/json'
}

#Create person

create_person_post = {
    'id': 4,
    'name': 'Erica',
    'email': 'erica@email.com',
    'login': 'erica123',
    'password': '12345'
}
json_data_post = json.dumps(create_person_post)
print(json_data_post)
conn.request("POST", "/persons/", json_data_post, headers=headers)#Crear una persona

#Friends of a person

#conn.request("GET", "/persons/1/friends", headers=headers)

#Friends of the friends of a person

#conn.request("GET", "/persons/0/mayYouKnow", headers=headers)

#Add a new relationship

#conn.request("POST", "/persons/person1/3/person2/4", headers=headers)

#Delete a relationship

#conn.request("POST", "/persons/delete/person1/3/person2/4", headers=headers)


start = datetime.datetime.now()
res = conn.getresponse()
end = datetime.datetime.now()

data = res.read()

elapsed = end - start

print(data.decode("utf-8"))
print("\"" + str(res.status) + "\"")
print("\"" + str(res.reason) + "\"")
print("\"elapsed seconds: " + str(elapsed) + "\"")

