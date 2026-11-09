#!/usr/bin/python3
"""
A script that uses a REST API (JSONPlaceholder) to export
todos of all employees into a JSON file.
"""

import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch all users
    users_res = requests.get("{}/users".format(base_url))
    users_data = users_res.json()

    # Fetch all todos
    todos_res = requests.get("{}/todos".format(base_url))
    todos_data = todos_res.json()

    # Dictionary to hold all tasks organized by user ID
    all_employees_dict = {}

    for user in users_data:
        user_id = user.get("id")
        username = user.get("username")

        # Filter todos for the current user
        user_todos = [
            t for t in todos_data
            if t.get("userId") == user_id
        ]

        task_list = []
        for task in user_todos:
            task_dict = {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            task_list.append(task_dict)

        all_employees_dict[str(user_id)] = task_list

    # Export to JSON file named todo_all_employees.json
    with open("todo_all_employees.json", mode="w", encoding="utf-8") as f:
        json.dump(all_employees_dict, f)
