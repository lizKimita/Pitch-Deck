from . import db


class Pitch:
    '''
    Pitch class to define the Pitch Objects
    '''
    all_pitches = []

    def __init__(self, pitch, postedOn):
        # self.author = author
        # self.category_name = category_name
        self.pitch = pitch
        self.postedOn = postedOn
        # self.upVote = upVote
        # self.downVote = downVote

    def save_pitch(self):
        Pitch.all_pitches.append(self)

    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()
    
    @classmethod
    def get_pitches(cls,name):
        
        response = []

        for pitch in cls.all_pitches:
            if pitch.category_name == name:
                response.append(pitch)

        return response

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))


    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    
    def __repr__(self):
        return f'User {self.name}'