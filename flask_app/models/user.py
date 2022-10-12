from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        users_from_db = connectToMySQL('users_db').query_db(query)
        users = []
        for user in users_from_db:
            users.append(cls(user))
        return users

    @staticmethod
    def get_one(userID):
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        user_from_db = connectToMySQL('users_db').query_db(query, userID)
        userInfo = []
        for info in user_from_db:
            userInfo.append(info)
        return userInfo

    @staticmethod
    def delete(userID):
        query = 'DELETE FROM users WHERE id = %(id)s;'
        connectToMySQL('users_db').query_db(query, userID)

    @classmethod
    def edit(cls, data):
        query = 'UPDATE users SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;'
        return connectToMySQL('users_db').query_db(query, data)

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO users (first_name, last_name, email) VALUES ( %(fname)s, %(lname)s, %(email)s );'
        return connectToMySQL('users_db').query_db(query, data)