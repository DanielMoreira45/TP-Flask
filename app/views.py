from .app import app
from flask import render_template
from .models import get_sample, get_sample2

@app.route("/")
def home():
    return render_template(
        "home.html", 
        title="My Anime !", 
        animes=get_sample2()
    )