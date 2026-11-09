#!/usr/bin/python3
"""
A script that uses a REST API (JSONPlaceholder) for a given employee ID,
and exports his/her TODO list progress into a CSV file.
"""

from csv import QUOTE_ALL, writer
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
    todos_res = requests.get(todos_url, params={"userId": employee_id})
    todos_data = todos_res.json()

    # File name format: USER_ID.csv
    file_name = "{}.csv".format(employee_id)

    # Write data to CSV file
    with open(file_name, mode="w", encoding="utf-8") as csv_file:
        csv_writer = writer(csv_file, quoting=QUOTE_ALL)
        for task in todos_data:
            completed = task.get("completed")
            title = task.get("title")
            csv_writer.writerow([employee_id, username, completed, title])
