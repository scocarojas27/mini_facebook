from repositories.UsersRepository import UsersRepository
from app import app


class UsersService(object):
    def __init__(self):
        self.users_repository = UsersRepository()

    def create_new_user(self, email, name, password, username):
        #print("Hola")
        return self.users_repository.create_new_user(email, name, password, username)

    def login(self,
              username,
              password):
        return self.users_repository.login(username,
                                           password)

    def get_user_by_id(self, id):
        return self.users_repository.get_user_by_id(id)

    def get_user_by_name(self, name):
        return self.users_repository.get_user_by_name(name)

    def get_all_users(self):
        return self.users_repository.get_all_users()

    def send_friend_request(self, userId1, userId2):
        return self.users_repository.send_friend_request(userId1, userId2)

    def friend_requests(self, id):
        return self.users_repository.friend_requests(id)
    
    def respond_friend_request(self, userId, requestId, status):
        return self.users_repository.respond_friend_request(userId, requestId, status)

    def users_count(self):
        response = self.users_repository.count()
        return int(response['count'])