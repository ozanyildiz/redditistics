from flask import render_template
import mongodb
from app import app

@app.route('/')
def index():
	stories = mongodb.get_stories()
	return render_template("index.html", stories=stories)
