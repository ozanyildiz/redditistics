from flask import Flask
from flask.ext.pymongo import PyMongo

app = Flask(__name__)

# mongodb configuration
app.config['MONGO_DBNAME'] = 'reddit'
mongo = PyMongo(app)

from app import views
