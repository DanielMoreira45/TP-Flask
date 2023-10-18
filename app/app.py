from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os.path

app = Flask(__name__)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
bootstrap = Bootstrap5(app)

def mkpath(p):
    return os.path.normpath(os.path.join(os.path.dirname(__file__ ),p))
app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///'+mkpath('../myapp.db'))
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = '3111990a-e74c-4366-8f1e-77c770304a87'

login_manager = LoginManager(app)
login_manager.login_view = "login"