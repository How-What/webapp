from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index = True, unique  = True)
    email = db.Column(db.String, unique = True)
    about_me = db.Column(db.String(150))
    password_hash = db.Column(db.String(150))

    def __init_(self):
        username = self.username
        password_hash = self.password_hash
        email = self.email
        about_me = self.about_me

    def set_password(self, password):
        '''
            generates the password has generated and sets it

            :password_hash: the password has generated
        '''
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        '''
            checks the passwords and see if it matches returns true if it does
        '''
        return check_password_hash(self.password_hash, password)
    
    @login.user_loader
    def load_user(id):
        return User.query.get(int(id)) 