import yaml, os.path
from .app import db, login_manager
from flask_login import UserMixin

Anime = yaml.safe_load(
    open(
        os.path.join(
            os.path.dirname(__file__),
            "anime.yml"
            )
        )
    )
# Pour avoir un id
i = 0
for anime in Anime:
    anime['id'] = i
    i += 1

def get_sample():
    return Anime[0:10]
  
from .app import db

class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def get_id(self):
        return self.id
    
    def __repr__(self):
        return "<Author (%d) %s>" % (self.id, self.name)

class Anime(db.Model):
    __tablename__ = 'anime'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    img = db.Column(db.String(100))
    nbEpisode = db.Column(db.Integer())
    dateS = db.Column(db.String(100))
    author_id = db.Column(db.Integer,db.ForeignKey("author.id"))
    author = db.relationship("Author", backref=db.backref("animes", lazy="dynamic"))
    
    def get_id(self):
        return self.id
    
    def __repr__(self):
        return "<Anime (%d) %s>"% (self.id, self.title)

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    username = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(64))

    def get_id(self):
        return self.username

def get_sample2():
    return Anime.query.limit(10).all()

def get_auteur(id):
    return Author.query.get(id)

def get_anime(id):
    return Anime.query.get(id)

def get_User(username):
    return User.query.get(username)

@login_manager.user_loader
def load_user(username):
    return User.query.get(username)
