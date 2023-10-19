from .app import app, db
from .models import get_sample, get_sample2, get_auteur, get_User, User

from flask import render_template, url_for, redirect, request
from flask_wtf import FlaskForm
from flask_login import login_user, logout_user, login_required

from wtforms import StringField, HiddenField, PasswordField
from wtforms.validators import DataRequired
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

    

@app.route("/")
def home():
    return render_template(
        "home.html", 
        title="My Anime !", 
        animes=get_sample2()
    )

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