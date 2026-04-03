from app.db.database import notes_collection

def save_note(content):
    note = {"content": content}
    notes_collection.insert_one(note)
    return "Note saved"

def get_notes():
    notes = list(notes_collection.find({}, {"_id": 0}))
    return notes