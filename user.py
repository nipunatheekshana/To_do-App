from flask_login import UserMixin
import dbms

# User class
class User(UserMixin):
    def __init__(self, username):
        dbUser=dbms.get('users',['id'], f"username = '{username}'")
        
        self.id = username
        self.userId=dbUser[0][0]
