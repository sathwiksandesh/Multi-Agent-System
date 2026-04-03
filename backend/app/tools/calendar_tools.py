from app.db.database import events_collection

def schedule_event(title, time):
    event = {
        "title": title,
        "time": time
    }
    events_collection.insert_one(event)
    return f"Event '{title}' scheduled at {time}"

def get_events():
    events = list(events_collection.find({}, {"_id": 0}))
    return events