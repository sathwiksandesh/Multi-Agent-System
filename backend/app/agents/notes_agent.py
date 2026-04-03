from app.tools.notes_tools import save_note, get_notes

def notes_agent(user_input):
    if "save note" in user_input:
        return save_note(user_input)
    elif "show notes" in user_input:
        return get_notes()
    return "Notes agent couldn't understand"