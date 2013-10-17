from flask import render_template
import mongodb
import dayops
from app import app

@app.route('/')
def index():
	today = dayops.get_today()
	yesterday = dayops.get_yesterday(today)
	tomorrow = dayops.get_tomorrow(today)
	stories = mongodb.get_all_stories()
	return render_template("index.html",
		page_title="Top stories of Yesterday", stories=stories,
		prev_day=yesterday, next_day=tomorrow)

@app.route('/<int:year>-<int:month>-<int:day>')
def archive(year, month, day):
	date = dayops.to_string(year, month, day)
	stories = mongodb.get_stories(date)
	return render_template("index.html", 
		page_title="Top stories of 17 Oct, 2013", stories=stories)
