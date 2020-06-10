from app import app
import db_config
import pika
import json
import sys
from datetime import datetime
from repositories.PublicationsRepository import PublicationsRepository

class PublicationsService(object):
    def __init__(self):
        self.publications_repository = PublicationsRepository()

    def send_publication(self,
                         publication):
        print("Hola 2")
        return self.publications_repository.send_publication(publication)

    def documents_count(self):
        response = self.publications_repository.count()
        app.logger.info("response {0}".format(response))
        return response

    def get_own_posts(self, id):
        return self.publications_repository.getOwnPosts(id)
    def get_friends_posts(self, id):
        return self.publications_repository.getFriendsPublications(id)