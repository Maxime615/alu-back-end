#!/usr/bin/python3
"""
A script that uses a REST API (JSONPlaceholder) for a given employee ID,
returns information about his/her TODO list progress, and displays it
on the standard output.
"""

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
    employee_name = user_data.get("name")

    # Fetch todos for the user
    todos_res = requests.get("{}/todos".format(base_url), params={"userId": employee_id})
    todos_data = todos_res.json()

    total_tasks = len(todos_data)
    completed_tasks = [t for t in todos_data if t.get("completed") is True]
    number_of_done_tasks = len(completed_tasks)

    # Display progress
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks))

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
