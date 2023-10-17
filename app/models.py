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

def get_sample():
    return Anime.query.limit(10).all()