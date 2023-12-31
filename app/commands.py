import click
from .app import app,db

@app.cli.command()
@click.argument('filename')
def loaddb(filename):
    '''Creates the tables and populates them with data.'''
    # création de toutes les tables
    db.create_all()
    import yaml
    from .models import Author, Anime
    Animes = yaml.safe_load(open(filename))
    # première passe: création de tous les auteurs
    authors = {}
    for b in Animes:
        a = b["author"]
        if a not in authors:
            o = Author(name=a)
            db.session.add(o)
            authors[a] = o
    db.session.commit()
    # deuxième passe: création de tous les animes
    for b in Animes:
        a = authors[b["author"]]
        o = Anime(title = b["title"],
                   img = b["img"],
                   nbEpisode = b["nbEpisodes"],
                   dateS= b["datesSortie"],
                   illustrator = b["illustrator"],
                   author_id = a.id)
        db.session.add(o)
    db.session.commit()

@app.cli.command()
@click.argument('username')
@click.argument('password')
def newuser(username,password):
    '''Add a new User'''
    from .models import User
    from hashlib import sha256
    m=sha256()
    m.update(password.encode())
    u = User(username=username, password=m.hexdigest())
    db.session.add(u)
    db.session.commit()
