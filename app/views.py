from flask import render_template
import mongodb
from dayops import *
from app import app

@app.route('/')
def index():
	today = get_today()
	stories = mongodb.get_stories(get_formatted_date(today))
	return render_template("index.html",
		page_title="Top stories of Yesterday", stories=stories,
		prev_day=get_prev_day(today), next_day=get_next_day(today))

@app.route('/<int:year>-<int:month>-<int:day>')
def archive(year, month, day):
	date = construct_datetime_obj(year, month, day)
	stories = mongodb.get_stories(get_formatted_date(date))
	return render_template("index.html",
		page_title="Top stories of 17 Oct, 2013", stories=stories,
		prev_day=get_prev_day(date), next_day=get_next_day(date))
