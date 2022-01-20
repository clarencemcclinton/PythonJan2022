from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        # ID field should be set to PK, NN, and AI in database so will be automatically generated
        self.id = data['id']

        # these are the main attributes that are unique to the individual instances
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.handle = data['handle']
        self.birthday = data['birthday']
        self.age = data['age']

        # these are also 'default' fields, but we need to give them values when updating or creating
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # =============================================
    # Get All Users from DB
    # =============================================
    @classmethod
    def all_users(cls):
        #1 - define your query
        query = "SELECT * FROM users;"

        #2 - call on the connectToMySQL to run query
        results = connectToMySQL('twitter').query_db(query)

        #2a - print raw response
        print(results)

        #3 - parse raw data into instance and store the instances in a new list
        users = []
        for user_data in  results:
            # User(user_data)
            # user = cls(user_data)
            users.append(cls(user_data))

        #4 - return new list of instances
        return users

    # =============================================
    # Get One User from DB based on ID
    # =============================================
    @classmethod
    def one_user(cls, data):
        #1 - define your query
        query = "SELECT * FROM users WHERE id = %(user_id)s;"

        #2 - call on the connectToMySQL to run query
        results = connectToMySQL('twitter').query_db(query, data)

        #2a - print raw response
        print(results)

        #4 - return instance of item at location 0 because you only queried for 1 item 
        # (see lecture about "Querying with Variables" for more explanation!)
        return cls(results[0])

    # =============================================
    # Add a New User to DB
    # =============================================
    @classmethod
    def create_user(cls, data):
        #1 - define your query
        query = "INSERT INTO users (first_name, last_name, handle, birthday, age, created_at) VALUES (%(first_name)s, %(last_name)s, %(handle)s, %(birthday)s, %(age)s, NOW());"
        
        #2 - call on the connectToMySQL to run query
        results = connectToMySQL('twitter').query_db(query, data)

        #2a - print raw response
        print(results)

        #4 - return query response - because this is an INSERT it will return the ID of the new record 
        return results

