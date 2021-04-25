from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from flask_login import UserMixin

#...

class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index=True)
    email = db.Column(db.String(255),unique=True,index=True)
    bio = db.Column(db.String(255))
    pitches = db.relationship('Pitch', backref='user', lazy='dynamic')
    pass_secure = db.Column(db.String(255))
    
    # profile_pic_path = db.Column(db.String())
    # role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    # reviews = db.relationship('Review',backref = 'user',lazy="dynamic")
    # pass_secure = db.Column(db.String(255))
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    
    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)
        
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
        

    def __repr__(self):
        return f'User {self.username}'
    
    
class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    pitch = db.Column(db.String(255))
    time = db.Column(db.DateTime, default = datetime.utcnow)
    category = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    # profile_pic_path = db.Column(db.String())
    # role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    # reviews = db.relationship('Review',backref = 'user',lazy="dynamic")
    # pass_secure = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.pitch}'
