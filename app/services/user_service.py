from app.utils.database import mongo
from app.models.user import User
from bson import ObjectId

class UserService:
    @staticmethod
    def get_all_users():
        users = mongo.db.users.find()
        return [User.from_dict(user) for user in users]

    @staticmethod
    def get_user_by_id(user_id):
        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        return User.from_dict(user) if user else None

    @staticmethod
    def create_user(user_data):
        user = User.from_dict(user_data)
        result = mongo.db.users.insert_one(user.to_dict())
        return str(result.inserted_id)

    @staticmethod
    def update_user(user_id, user_data):
        user = User.from_dict(user_data)
        mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": user.to_dict()})

    @staticmethod
    def delete_user(user_id):
        mongo.db.users.delete_one({"_id": ObjectId(user_id)})
