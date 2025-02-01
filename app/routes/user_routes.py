from flask import Blueprint, request, jsonify
from app.services.user_service import UserService
from bson import ObjectId

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = UserService.get_all_users()
    return jsonify([user.__dict__ for user in users])

@user_bp.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = UserService.get_user_by_id(user_id)
    if user:
        return jsonify(user.__dict__)
    return jsonify({"error": "User not found"}), 404

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user_id = UserService.create_user(data)
    return jsonify({"id": user_id}), 201

@user_bp.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    UserService.update_user(user_id, data)
    return jsonify({"message": "User updated"})

@user_bp.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    UserService.delete_user(user_id)
    return jsonify({"message": "User deleted"})
