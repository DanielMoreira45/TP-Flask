from .app import app, db
from flask import render_template, url_for, redirect
from .models import get_sample, get_sample2, get_auteur, Author
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired

class AuthorFrom(FlaskForm):
    id = HiddenField('id')
    name = StringField('Nom',validators=[DataRequired()])

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