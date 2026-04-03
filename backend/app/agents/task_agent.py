from app.tools.task_tools import create_task, get_tasks

def task_agent(user_input):
    if "create" in user_input or "add task" in user_input:
        return create_task(user_input)
    elif "show tasks" in user_input:
        return get_tasks()
    return "Task agent couldn't understand"