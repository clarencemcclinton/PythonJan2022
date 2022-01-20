from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']

        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.handle = data['handle']
        self.birthday = data['birthday']
        self.age = data['age']

        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # =============================================
    # Get All Users from DB
    # =============================================
    @classmethod
    def all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('twitter').query_db(query)
        print(results)
        users = []
        for user_data in  results:
            # User(user_data)
            # user = cls(user_data)
            users.append(cls(user_data))
        return users

    # =============================================
    # Get One User from DB based on ID
    # =============================================
    @classmethod
    def one_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(user_id)s;"
        results = connectToMySQL('twitter').query_db(query, data)
        print(results)
        return cls(results[0])

    # =============================================
    # Add a New User to DB
    # =============================================
    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, handle, birthday, age, created_at) VALUES (%(first_name)s, %(last_name)s, %(handle)s, %(birthday)s, %(age)s, NOW());"
        results = connectToMySQL('twitter').query_db(query, data)
        print(results)
        return results

