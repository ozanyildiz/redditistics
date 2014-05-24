import json
import urllib2
import time
import pymongo
import re
import os

def get_db_stories():
    MONGO_URI = os.environ.get('MONGO_URI')
    if MONGO_URI:
        connection = pymongo.Connection(MONGO_URI, safe=True)
    else:
        connection = pymongo.Connection("mongodb://localhost", safe=True) #when working at local

    db = connection.reddit
    return db.stories

def get_front_page_stories():
    reddit_page = urllib2.urlopen("http://www.reddit.com/.json")
    parsed = json.load(reddit_page)
    return parsed['data']['children']

def get_pruned_story(story_data):
    s = dict()
    s['title'] = story_data['title']
    s['url'] = story_data['url']
    s['subreddit'] = story_data['subreddit']
    thumbnail = story_data['thumbnail']
    if re.search('jpg', thumbnail):
        s['thumbnail'] = story_data['thumbnail']
    else:
        s['thumbnail'] = ''
    s['domain'] = story_data['domain']
    s['score'] = story_data['score']
    s['permalink'] = story_data['permalink']
    s['num_comments'] = story_data['num_comments']
    s['created_epoch'] = story_data['created']
    s['created'] = time.strftime('%Y-%m-%d', time.gmtime(story_data['created']))

    return s

stories = get_db_stories()
try:
    raw_stories = get_front_page_stories()
    for story in raw_stories:
        pruned_story = get_pruned_story(story['data'])
        stories.update({'permalink': pruned_story['permalink']}, pruned_story, True)
    print "Stories updated successfully.", time.strftime("%d/%m/%Y %H:%M:%S")
except Exception as e:
    print e
    print "Stories cannot updated successfully.", time.strftime("%d/%m/%Y %H:%M:%S")

