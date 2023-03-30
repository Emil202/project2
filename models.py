from extensions import db,login_manager
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

class Image(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    image_name = db.Column(db.String(255),nullable = False)
    
    
    def __init__(self,image_name ):
        self.image_name = image_name
      
        

    def __repr__(self):
        return self.image_name


    def save(self):
        db.session.add(self)
        db.session.commit()
        

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False,unique = True)
    password = db.Column(db.String(255), nullable = False)
    is_active = db.Column(db.Boolean, default = True )
    is_superuser =  db.Column(db.Boolean, default = True )

    def __init__(self, full_name, email, password):
        self.full_name = full_name
        self.email = email
        self.password= generate_password_hash(password)
      

    
    def check_password(self,password):
        return check_password_hash(self.password,password)

    def __repr__(self):
        return self.name

    def save(self):
        db.session.add(self)
        db.session.commit()



class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String(100),nullable = False)
    email = db.Column(db.String(100),nullable = False,unique = True)
    message = db.Column(db.String(255),nullable = False)


    def __init__(self, full_name, email,message):
        self.full_name = full_name
        self.email = email
        self.message = message
        

    def __repr__(self):
        return self.email


    def save(self):
        db.session.add(self)
        db.session.commit()