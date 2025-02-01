from bson import ObjectId

class User:
    def __init__(self, name, email, password, address):
        self.name = name
        self.email = email
        self.password = password
        self.address = address

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "address":self.address
        }

    @staticmethod
    def from_dict(data):
        return User(
            name=data.get("name"),
            email=data.get("email"),
            password=data.get("password")
            address=data.get("address")
        )
