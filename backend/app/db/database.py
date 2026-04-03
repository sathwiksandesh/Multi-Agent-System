from pymongo import MongoClient

MONGO_URL = "mongodb+srv://sathwiksiddhantam_db_user:cP4V4mxXar9RrzOR@cluster0.7jg8lov.mongodb.net/?appName=Cluster0"

client = MongoClient(MONGO_URL)

db = client["ai_agent_db"]

tasks_collection = db["tasks"]
events_collection = db["events"]
notes_collection = db["notes"]