import yaml, os.path

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
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __repr__(self):
        return "<Author (%d) %s>" % (self.id, self.name)

class Anime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    img = db.Column(db.String(100))
    nbEpisode = db.Column(db.Integer())
    dateS = db.Column(db.String(100))
    author_id = db.Column(db.Integer,db.ForeignKey("author.id"))
    author = db.relationship("Author", backref=db.backref("animes", lazy="dynamic"))

    def __repr__(self):
        return "<Book (%d) %s>"% (self.id, self.title)

def get_sample2():
    return Anime.query.limit(10).all()

def get_auteur(id):
    return Author.query.get(id)
