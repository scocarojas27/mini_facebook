import pymysql
from db_config import mysql
import json
import http.client

conn = mysql.connect()
cursor = conn.cursor()

conn_neo4j = http.client.HTTPConnection("localhost:5000")

headers = {
    'Content-type': 'application/json'
}

def daemon():
    query = "SELECT user_id_origin, user_id_target FROM friend_requests WHERE status='accepted';"
    try:
        cursor.execute(query)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        #print(results)
        for i in range(len(results)):
            userId1 = results[i][0]
            userId2 = results[i][1]
            url = "/persons/person1/" + str(userId1) + "/person2/" + str(userId2)
            conn_neo4j.request("POST", url, headers=headers)
    except:
        print("Error! Unable to fetch data") 
    return 0

daemon()  


