from flask import render_template, jsonify
import mongodb
from dayops import *
from app import app

@app.route('/')
@app.route('/<int:year>-<int:month>-<int:day>')
def archive(year=get_today().year, month=get_today().month, day=get_today().day):
    date = construct_datetime_obj(year, month, day)
    print date
    print get_formatted_date(date)
    stories = mongodb.get_stories(get_formatted_date(date))
    popular_subreddits = mongodb.get_popular_subreddits(get_formatted_date(date))
    page_title = "Top stories of " + get_prettified(date)
    return render_template("index.html",
        page_title=page_title, stories=stories, popular_subreddits=popular_subreddits,
        prev_day=get_prev_day(date), next_day=get_next_day(date),
        is_today=is_today(date))

@app.route('/api')
def api_page():
    return render_template('api_page.html')

@app.route('/stories/<int:year>-<int:month>-<int:day>')
def get_stories(year, month, day):
    date = construct_datetime_obj(year, month, day)
    stories = mongodb.get_stories(get_formatted_date(date))
    return jsonify({'stories': mongodb.json_encoder(stories)})