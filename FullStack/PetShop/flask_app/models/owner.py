from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import pet

class Owner:
    db = "owners_pets_schema"
    def __init__(self, data):
        self.id = data['id']

        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.pets = []

    @classmethod
    def owners_with_pets(cls):
        query = "SELECT * FROM owners LEFT JOIN pets ON owners.id = pets.owner_id ORDER BY owners.id DESC;"
        results = connectToMySQL(cls.db).query_db(query)
        # print(results)
        owners = []
        owner_ids = []

        for data in results:
            if data['id'] not in owner_ids:
                owner_ids.append(data['id'])
                owners.append(cls(data))
            pet_data = {
                "id" : data["pets.id"],
                "name" : data["name"],
                "type" : data["type"],
                "age" : data["pets.age"],
                "created_at" : data["pets.created_at"],
                "updated_at" : data["pets.updated_at"],
                "owner_id" : data["owner_id"]
            }
            owners[len(owners)-1].pets.append(pet.Pet(pet_data))

        return owners

    @classmethod
    def get_one_owner(cls, data):
        query = "SELECT * FROM owners LEFT JOIN pets ON owners.id = pets.owner_id WHERE owners.id = %(owner_id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        owner = cls( results[0] )
        for pet_info in results:
            pet_data = {
                "id" : pet_info["pets.id"],
                "name" : pet_info["name"],
                "type" : pet_info["type"],
                "age" : pet_info["pets.age"],
                "created_at" : pet_info["pets.created_at"],
                "updated_at" : pet_info["pets.updated_at"],
                "owner_id" : pet_info["owner_id"]
            }
            owner.pets.append(pet.Pet(pet_data))
        return owner