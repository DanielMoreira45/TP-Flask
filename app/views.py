import os.path

from .app import app, db
from .models import get_sample2, get_auteur, get_User, User, Author, Anime

from flask import render_template, url_for, redirect, request
from flask_wtf import FlaskForm
from flask_login import login_user, logout_user, login_required

from wtforms import StringField, HiddenField, PasswordField, SelectField, FileField, IntegerField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename
from hashlib import sha256

class AuthorFrom(FlaskForm):
    id = HiddenField('id')
    name = StringField('Nom',validators=[DataRequired()])

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    next = HiddenField()

    def get_authenticated_user(self):
        user = User.query.get(self.username.data)
        if user is None:
            return None
        m = sha256()
        m.update(self.password.data.encode())
        passwd = m.hexdigest()
        return user if passwd == user.password else None

class InscriptionForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    next = HiddenField()

    def create_user(self):
        m = sha256()
        m.update(self.password.data.encode())
        user = User(username=self.username.data, password=m.hexdigest())
        if user is None:
            return None
        existing_user = User.query.filter_by(username=self.username.data).first()
        if existing_user:
            return None
        else:
            db.session.add(user)
            db.session.commit()

class UploadAnimeForm(FlaskForm):
    auteur = StringField('Auteur')
    illustrateur = StringField('Illustrateur')
    nb_episodes = IntegerField('Nombre d\'épisodes')
    titre = StringField('Titre')
    date_debut = SelectField('Date de début', choices=[(str(year), str(year)) for year in range(1950, 2023)])
    date_fin = SelectField('Date de fin', choices=[(str(year), str(year)) for year in range(1950, 2023)])
    image = FileField('Imagede l\'anime')


@app.route("/")
def home():
    return render_template(
        "home.html", 
        title="My Anime !", 
        animes=get_sample2()
    )

@app.route("/detail/<id>")
def detail(id):
    animes = get_sample2()
    anime = animes[int(id)-1]
    return render_template("detail.html",anime=anime)

@app.route("/edit/author/<int:id>")
@login_required
def edit_author(id):
    a = get_auteur(id)
    f = AuthorFrom(id =a.id,name=a.name)
    return render_template("edit-author.html",author=a,form=f)

@app.route("/save/author/", methods =("POST",))
def save_author():
    a = None
    f = AuthorFrom()
    if f.validate_on_submit():
        id = int(f.id.data)
        a = get_auteur(id)
        a.name = f.name.data
        db.session.commit()
        return redirect(url_for('home'))
    a = get_auteur(int(f.id.data))
    return render_template("edit-author.html",author =a, form=f)

@app.route("/login/", methods = ("GET","POST",))
def login():
    f = LoginForm()
    if not f.is_submitted():
        f.next.data = request.args.get("next")
    elif f.validate_on_submit():
        user = f.get_authenticated_user()
        if user:
            login_user(user)
            next = f.next.data or url_for("home")
            return redirect(next)
    return render_template("login.html", form=f)

@app.route("/logout/")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/inscription/", methods = ("GET","POST",))
def inscription():
    f = InscriptionForm()
    if not f.is_submitted():
        f.next.data = request.args.get("next")
    elif f.validate_on_submit():
        f.create_user()
        return redirect(url_for("login"))
    return render_template("inscription.html", form=f)

@app.route('/upload/', methods = ("GET","POST",))
def upload_file():
    f = UploadAnimeForm()
    print(f.validate_on_submit())
    if f.validate_on_submit():
        auteur = f.auteur.data
        illustrateur = f.illustrateur.data
        nb_episodes = f.nb_episodes.data
        titre = f.titre.data
        date_debut = f.date_debut.data
        date_fin = f.date_fin.data

        if 'image' in request.files:
            image = request.files['image']
            if image:
                filename = secure_filename(image.filename)
                file_path = os.path.join('static', 'img', filename)
                image.save(file_path)
                dateS = date_debut+" - "+date_fin
                author = Author(name=auteur)
                if author:
                    db.session.add(author)
                    db.session.commit()
                    print(titre)
                    print(filename)
                    print(nb_episodes)
                    print(dateS)
                    print(illustrateur)
                    print(author.get_id())
                    anime = Anime(title=titre,img=filename,nbEpisode=nb_episodes,dateS=dateS,illustrator=illustrateur,author_id=author.get_id())
                    print("proche anime")
                    if anime:
                        db.session.add(anime)
                        db.session.commit()
                        return redirect(url_for('home'))


    return render_template('anime_form.html', form=f)
