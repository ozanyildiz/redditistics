from app import mongo
import json
from bson import json_util

def get_all_stories():
    return mongo.db.stories.find()

def get_stories(date):
    return mongo.db.stories.find({'created': date}).sort("score", -1)

def json_encoder(cursor):
    json_docs = []
    for doc in cursor:
        json_doc = json.dumps(doc, default=json_util.default)
        json_docs.append(json_doc)
    return json_docs
