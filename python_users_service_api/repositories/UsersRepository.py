import pymysql
from db_config import mysql

class UsersRepository(object):
    def __init__(self):
        self.conn = mysql.connect()

    def create_new_user(self, email, name, password, username):
        #Inserta un nuevo usuario a la base de datos y retorna su información
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("INSERT INTO user(email, name, password, username) SELECT %s, %s, %s, %s FROM dual WHERE NOT EXISTS (SELECT * FROM user WHERE username = %s AND email = %s)", (email, name, password, username, username, email))
        self.conn.commit()
        cursor.execute("select * from user where email=%s and username=%s",(email, username))
        rows = cursor.fetchone()
        cursor.close()
        return rows

    def login(self, username, password):
        #Consulta que el usuario exista en la base de dato y verifica sus credenciales
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id AS id FROM user WHERE username=%s AND password=%s", (username, password))
        row = cursor.fetchone()
        cursor.close()
        return row

    def get_user_by_id(self, id):
        #Consulta un usuario basado en su id
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT email, name, username FROM user WHERE id=%s", id)
        row = cursor.fetchone()
        cursor.close()
        return row

    def get_user_by_name(self, name):
        #Consulta usuarios basados en su nombre
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT email, name, username FROM user WHERE name=%s", name)
        row = cursor.fetchone()
        cursor.close()
        return row

    def get_all_users(self):
        #Consulta todos los usuarios
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT email, name, username FROM user")
        rows = cursor.fetchone()
        cursor.close()
        return rows

    def send_friend_request(self, userId1, userId2):
        #Inserta una nueva relación de amistad en la base de datos
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("INSERT INTO friend_requests(user_id_origin, user_id_target, status, create_date, update_date) SELECT %s, %s, 'sent', CURDATE(), CURDATE() FROM dual WHERE NOT EXISTS (SELECT * FROM friend_requests WHERE user_id_origin = %s AND user_id_target = %s)", (userId1, userId2, userId1, userId2))
        self.conn.commit()
        cursor.execute("select * from friend_requests where user_id_origin=%s and user_id_target=%s", (userId1, userId2))
        row = cursor.fetchone()
        cursor.close()
        return row

    def friend_requests(self, id):
        #Consulta las solicitudes de amistad de un usuario
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM friend_requests WHERE user_id_target=%s", id)
        rows = cursor.fetchone()
        cursor.close()
        return rows

    def respond_friend_request(self, userId, requestId, status):
        #Modifica el estado de la solicitud de amistad, dependidendo de la respuesta del usuario
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("UPDATE friend_requests SET status=%s WHERE id=%s and user_id_target=%s", (status, requestId, userId))
        self.conn.commit()
        cursor.execute("select * from friend_requests where user_id_origin=%s and user_id_target=%s", (userId1, userId2))
        row = cursor.fetchone()
        cursor.close()
        return row

    def count(self):
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT count(id) as count FROM user")
        row = cursor.fetchone()
        cursor.close()
        return row