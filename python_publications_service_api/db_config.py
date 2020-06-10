from app import app
from flask_jwt_extended import JWTManager

app.config['mongodb_url'] = "mongodb://localhost:27017/"
app.config['mongodb_username'] = 'root'
app.config['mongodb_password'] = 'example'

# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = 'mySecretKey'  # Change this!
app.config['JWT_ALGORITHM'] = 'HS512'
app.config['JWT_EXP_DELTA_SECONDS'] = 60
app.config['JWT_TOKEN_LOCATION'] = ['cookies', 'headers']
jwt = JWTManager(app)