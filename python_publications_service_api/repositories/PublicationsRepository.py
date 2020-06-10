from pymongo import MongoClient
from app import app
import db_config
import http.client
from bson import json_util, ObjectId
import json

class PublicationsRepository(object):
    def __init__(self):
        self.client = MongoClient(app.config['mongodb_url'])
        
    def count(self):
        print("count all publications...")
        db = self.client['publicationsDB']
        return db.publications.count_documents({})

    def send_publication(self, publication):
        print('Está mal')
        db = self.client['publicationsDB']
        #print(str(db))
        db = db['posts']
        print(str(db))
        #results = db.insert_one(publication)
        #print(results.inserted_id)
        return results

    def getFriendsPublications(self, id):
        #Se obtienen los amigos con un request a otra api, suongo yo que es un get
        conn_neo4j = http.client.HTTPConnection("localhost:5000")
        url = "/persons/" + str(id) + "/friends"
        conn_neo4j.request("GET", url, headers={'Content-type': 'application/json'})
        res = conn_neo4j.getresponse()
        data = res.read()
        data_json = json.loads(data.decode("utf-8"))
        friends = []
        print(data_json)
        for f in data_json:
            print(f['id'])
            friends.append(f['id']) #ese "user_id" se cambia por el id del amigo, o sea su propiedad
        return self.getFriendsPosts(friends)

    def getFriendsPosts(self, friends):
        db = self.client["publicationsDB"]
        db = db["posts"]
        posts = []
        for f in friends:
            cursor = db.find({"user_id" : f}, {"_id" : 0})
            new_cursor = json.loads(json_util.dumps(cursor))
            #print(new_cursor)
            for p in new_cursor:
                posts.append(p)
        return posts

    def getOwnPosts(self, id) :
        db = self.client["publicationsDB"]
        db = db["posts"]
        cursor = db.find({"user_id" : id}, {"_id" : 0})
        new_cursor = json.loads(json_util.dumps(cursor))
        posts = []
        for p in new_cursor: 
            posts.append(p)
        return posts
