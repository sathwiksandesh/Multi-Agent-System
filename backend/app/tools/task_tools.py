from app.db.database import tasks_collection

def create_task(title, deadline=None):
    task = {
        "title": title,
        "deadline": deadline,
        "status": "pending"
    }
    tasks_collection.insert_one(task)
    return f"Task '{title}' created"

def get_tasks():
    tasks = list(tasks_collection.find({}, {"_id": 0}))
    return tasks