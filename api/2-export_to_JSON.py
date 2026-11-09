#!/usr/bin/python3
"""
A script that uses a REST API (JSONPlaceholder) for a given employee ID,
and exports his/her TODO list progress into a JSON file.
"""

import json
from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) < 2:
        exit(1)

    try:
        employee_id = int(argv[1])
    except ValueError:
        exit(1)

    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user details
    user_res = requests.get("{}/users/{}".format(base_url, employee_id))
    user_data = user_res.json()
    username = user_data.get("username")

    # Fetch todos for the user
    todos_url = "{}/todos".format(base_url)
    todos_res = requests.get(
        todos_url,
        params={"userId": employee_id}
    )
    todos_data = todos_res.json()

    # Build the task list matching the required structure
    task_list = []
    for task in todos_data:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        task_list.append(task_dict)

    # Export to JSON file named USER_ID.json
    file_name = "{}.json".format(employee_id)
    with open(file_name, mode="w", encoding="utf-8") as json_file:
        json.dump({str(employee_id): task_list}, json_file)
