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
    todos_res = requests.get("{}/todos".format(base_url), params={"userId": employee_id})
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

    # Wrap in dictionary with employee_id as key
    out_data = {str(employee_id): task_list}

    # File name format: USER_ID.json
    file_name = "{}.json".format(employee_id)

    # Write data to JSON file
    with open(file_name, mode="w", encoding="utf-8") as json_file:
        json.dump(out_data, json_file)
