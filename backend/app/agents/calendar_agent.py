from app.tools.calendar_tools import schedule_event, get_events

def calendar_agent(user_input):
    if "schedule" in user_input:
        return schedule_event(user_input, "10:00 AM")
    elif "show events" in user_input:
        return get_events()
    return "Calendar agent couldn't understand"