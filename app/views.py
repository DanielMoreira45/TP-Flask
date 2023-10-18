from .app import app, db
from .models import get_sample, get_sample2, get_auteur, User

from flask import render_template, url_for, redirect
from flask_wtf import FlaskForm
from flask_login import login_user, logout_user, current_user

from wtforms import StringField, HiddenField, PasswordField
from wtforms.validators import DataRequired
from hashlib import sha256

class AuthorFrom(FlaskForm):
    id = HiddenField('id')
    name = StringField('Nom',validators=[DataRequired()])

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')

    def get_authenticated_user(self):
        user = User.query.get(self.username.data)
        if user is None:
            return None
        m = sha256()
        m.update(self.password.data.encode())
        passwd = m.hexdigest()
        return user if passwd == user.password else None

@app.route("/")
def home():
    return render_template(
        "home.html", 
        title="My Anime !", 
        animes=get_sample2()
    )

@app.route("/edit/author/<int:id>")
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
    if f.validate_on_submit():
        user = f.get_authenticated_user()
        if user:
            login_user(user)
            return redirect(url_for("home"))
    return render_template("login.html", form=f)

@app.route("/logout/")
def logout():
    logout_user()
    return redirect(url_for('home'))