from .app import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

class Anime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    img = db.Column(db.String(100))
    nbEpisode = db.Column(db.Integer(100))
    dateS = db.Column(db.String(100))
    author_id = db.Column(db.Integer,db.ForeignKey("author.id"))
    author = db.relationship("Author", backref=db.backref("animes", lazy="dynamic"))

def get_sample():
    return Anime.query.limit(10).all()