from app import app
from flask import request, jsonify
from controllers.GatewayApi import gateway_api

app.register_blueprint(gateway_api)

if __name__ == "__main__":
    app.run(debug=True,
            host='0.0.0.0',
            port=5030)