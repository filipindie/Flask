from flask import Flask
from peewee import *
from app.models import tables #importando as tabelas do bd
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')

login_manager = LoginManager(app)


tables.initialize_pg_db() #cria as tables

from app.models import tables, forms
from app.controllers import default

