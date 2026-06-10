from datetime import datetime
from validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

tasks = []

def add_task(title, description, due_date):
    if not validate_task_title(title):
        print("Invalid title")
        return

    if not validate_task_description(description):
        print("Invalid description")
        return

    if not validate_due_date(due_date):
        print("Invalid due date")
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")

def mark_task_as_complete(index, tasks=tasks):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task index")

def view_pending_tasks(tasks=tasks):
    for task in tasks:
        if not task["completed"]:
            print(task)

def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        progress = 0
    else:
        completed = sum(1 for task in tasks if task["completed"])
        progress = (completed / len(tasks)) * 100

    return progress