from flask_app.config.mysqlconnection import connectToMySQL

class Pet:
    def __init__(self, data):
        self.id = data["id"]

        self.name = data["name"]
        self.type = data["type"]
        self.age = data["age"]

        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
        self.owner_id = data["owner_id"]