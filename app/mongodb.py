from app import mongo

def get_all_stories():
    return mongo.db.stories.find()

def get_stories(date):
    return mongo.db.stories.find({'created': date})

