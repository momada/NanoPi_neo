# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app import views, models


app = Flask(__name__)

# Configuration of application, see configuration.py, choose one and uncomment.
# app.config.from_object('configuration.ProductionConfig')
app.config.from_object('app.configuration.DevelopmentConfig')
# app.config.from_object('configuration.TestingConfig')

bs = Bootstrap(app)  # flask-bootstrap
db = SQLAlchemy(app)  # flask-sqlalchemy

lm = LoginManager()
lm.init_app(app)
lm.login_message = "You must be logged in to access this page."
lm.login_view = 'login'


