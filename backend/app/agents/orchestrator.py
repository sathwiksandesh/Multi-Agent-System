from app.agents.task_agent import task_agent
from app.agents.calendar_agent import calendar_agent
from app.agents.notes_agent import notes_agent

def run_agent(user_input):
    user_input = user_input.lower()

    # Multi-step workflow example
    if "plan my day" in user_input:
        tasks = task_agent("show tasks")
        events = calendar_agent("show events")
        return {
            "tasks": tasks,
            "events": events,
            "message": "Here is your plan for the day"
        }

    # Routing
    if "task" in user_input:
        return task_agent(user_input)

    elif "schedule" in user_input or "event" in user_input:
        return calendar_agent(user_input)

    elif "note" in user_input:
        return notes_agent(user_input)

    return "I couldn't understand your request"