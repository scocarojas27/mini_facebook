from app import app
from flaskext.mysql import MySQL
from flask_jwt_extended import JWTManager

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'UsersDB'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'   #'localhost' 'MySQLServiceDB'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_USE_POOL'] = {
    #use = 0 no pool else use pool
    'use': 1,
    # size is >=0,  0 is dynamic pool
    'size': 10,
    #pool name
    'name': 'local'
}
mysql.init_app(app)