from datetime import datetime
from missingprofessor import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    prog = db.Column(db.Integer, nullable=False, default=0)
    password = db.Column(db.String(60), nullable=False)
    housekey = db.Column(db.Boolean, unique=False, nullable=False, default=False)
    dogpic = db.Column(db.Boolean, unique=False, nullable=False, default=False)
    diary = db.Column(db.Boolean, unique=False, nullable=False, default=False)
    labkeywrong = db.Column(db.Integer, nullable=False, default=0)
    factorykeywrong = db.Column(db.Integer, nullable=False, default=0)
    labaudio = db.Column(db.Boolean, unique=False, nullable=False, default=False)
    mansion = db.Column(db.Boolean, unique=False, nullable=False, default=False)
    warehouse = db.Column(db.Boolean, unique=False, nullable=False, default=False)
    deadendsmet = db.Column(db.Integer, nullable=False, default=0)
    endingreached = db.Column(db.Boolean, unique=False, nullable=False, default=False)
    
    analytics = db.relationship('Analytics', backref='player', lazy=True)
    def __repr__(self):
        return f"User(User_id  = '{self.id}','username = {self.username}', 'email = {self.email}','ending reached = {self.endingreached}', 'progress = {self.prog}', 'diary = {self.diary}','lab key wrong = {self.labkeywrong}', 'factory key wrong = {self.factorykeywrong}', 'dead ends met = {self.deadendsmet} out of 2')" 


class Analytics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    progress = db.Column(db.String(20), unique=True, nullable=False)
    def __repr__(self):
        return f"User({self.user_id}, {self.progress})"
