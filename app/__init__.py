from flask import Flask
from flask.ext.pymongo import PyMongo
import os

app = Flask(__name__)

# mongodb configuration

MONGO_URI = os.environ.get('MONGO_URI')
if MONGO_URI:
    app.config['MONGO_URI'] = MONGO_URI
else:
    app.config['MONGO_DBNAME'] = 'reddit' #when working at local

mongo = PyMongo(app)

from app import views
