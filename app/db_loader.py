import json
import urllib2
import time
import pymongo

AN_HOUR = 3600 # in seconds

def get_db_stories():
    connection = pymongo.Connection("mongodb://localhost", safe=True)
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
    s['thumbnail'] = story_data['thumbnail']
    s['domain'] = story_data['domain']
    s['score'] = story_data['score']
    s['permalink'] = story_data['permalink']
    s['num_comments'] = story_data['num_comments']
    s['created_epoch'] = story_data['created']
    s['created'] = time.strftime('%Y-%m-%d', time.gmtime(story_data['created']))

    return s

def main():
    stories = get_db_stories()
    #while True:
    raw_stories = get_front_page_stories()
    for story in raw_stories:
        pruned_story = get_pruned_story(story['data'])
        #print pruned_story
        stories.update({'permalink': pruned_story['permalink']}, pruned_story, True)
#time.sleep(AN_HOUR)


if __name__ == "__main__":
    main()
