from app import mongo

def get_stories():
	return mongo.db.stories.find()
