from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
    get_jwt
)

from models.user_model import db, User

auth_bp = Blueprint("auth", __name__)

# ---------------- REGISTER ---------------- #

@auth_bp.route("/register", methods=["POST"])
def register():
    """
    User Registration API
    ---
    tags:
      - Authentication

    parameters:
      - in: body
        name: body
        required: true

        schema:
          type: object

          properties:
            username:
              type: string
              example: vivek@gmail.com

            password:
              type: string
              example: Password123

            role:
              type: string
              example: admin

    responses:
      201:
        description: User registered successfully

      400:
        description: User already exists
    """
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")
    role = data.get("role", "user")

    if User.query.filter_by(username=username).first():
        return jsonify({
            "message": "User already exists"
        }), 400

    new_user = User(
        username=username,
        role=role
    )

    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "message": "User registered successfully"
    }), 201

# ---------------- LOGIN ---------------- #

@auth_bp.route("/login", methods=["POST"])
def login():
    """
    User Login API
    ---
    tags:
      - Authentication

    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            username:
              type: string
              example: vivek

            password:
              type: string
              example: Password123

    responses:
      200:
        description: Login successful

        schema:
            type: object

        properties:
            access_token:
                type: string
      401:
        description: Invalid credentials
    """

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):

        access_token = create_access_token(
            identity=str(user.username),
            additional_claims={
                "role": str(user.role)
            }
        )

        return jsonify({
            "access_token": access_token
        }), 200

    return jsonify({
        "message": "Invalid credentials"
    }), 401

# ---------------- DASHBOARD ---------------- #

@auth_bp.route("/dashboard", methods=["GET"])
@jwt_required()
def dashboard():
    """
    User Dashboard API
    ---
    tags:
      - Dashboard

    security:
      - Bearer: []

    responses:
      200:
        description: Dashboard accessed successfully

        schema:
          type: object

          properties:
            message:
              type: string
              example: Welcome vivek

      401:
        description: Unauthorized
    """
    current_user = get_jwt_identity()

    return jsonify({
        "message": f"Welcome {current_user}"
    })

# ---------------- ADMIN ---------------- #

@auth_bp.route("/admin", methods=["GET"])
@jwt_required()
def admin():
    """
    Admin Access API
    ---
    tags:
      - Admin

    security:
      - Bearer: []

    responses:
      200:
        description: Admin access granted

        schema:
          type: object

          properties:
            message:
              type: string
              example: Welcome Admin

      403:
        description: Admin access denied

      401:
        description: Unauthorized
    """
    claims = get_jwt()

    if claims["role"] != "admin":
        return jsonify({
            "message": "Admins only"
        }), 403

    return jsonify({
        "message": "Welcome Admin"
    })