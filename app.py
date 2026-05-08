from flask import Flask
from flask_jwt_extended import JWTManager
from flasgger import Swagger

from models.user_model import db
from routes.auth_routes import auth_bp

import config

app = Flask(__name__)

# ---------------- CONFIG ---------------- #

app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS
app.config["JWT_SECRET_KEY"] = config.JWT_SECRET_KEY

# ---------------- INIT ---------------- #

db.init_app(app)

jwt = JWTManager(app)

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "SecureAuth API",
        "description": "JWT Authentication API Documentation",
        "version": "1.0"
    },

    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "Enter: Bearer <JWT_TOKEN>"
        }
    }
}
swagger = Swagger(app, template=swagger_template)

# ---------------- REGISTER BLUEPRINT ---------------- #

app.register_blueprint(auth_bp)

# ---------------- CREATE DATABASE ---------------- #

with app.app_context():
    db.create_all()

# ---------------- RUN ---------------- #

if __name__ == "__main__":
    app.run(debug=True)