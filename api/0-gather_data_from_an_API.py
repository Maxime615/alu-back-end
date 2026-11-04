#!/usr/bin/python3
"""
A script that uses a REST API (JSONPlaceholder) for a given employee ID,
returns and displays his/her TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user details
    user_url = "{}/users/{}".format(base_url, employee_id)
    user_name = requests.get(user_url).json().get("name")

    # Fetch todos
    todos_url = "{}/todos".format(base_url)
    todos = requests.get(todos_url, params={"userId": employee_id}).json()

    total_tasks = len(todos)
    done_tasks = [t for t in todos if t.get("completed") is True]
    number_of_done_tasks = len(done_tasks)

    print(
        "Employee {} is done with tasks({}/{}):".format(
            user_name, number_of_done_tasks, total_tasks
        )
    )

    for task in done_tasks:
        print("\t {}".format(task.get("title")))
