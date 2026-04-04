from pymongo import MongoClient

MONGO_URL = "YOUR_URL"

client = MongoClient(MONGO_URL)

db = client["ai_agent_db"]

tasks_collection = db["tasks"]
events_collection = db["events"]
notes_collection = db["notes"]
