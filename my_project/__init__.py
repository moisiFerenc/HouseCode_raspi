from flask import Flask, render_template, request
from flask_login import UserMixin, LoginManager, login_manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import time
import multiprocessing as mp
import serial
import flask_bcrypt as Bcrypt
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
Migrate(app, db)

login_manager.init_app(app)
login_manager.login_view = 'login'

