#!/usr/bin/python3
"""Module to export TODO list from API in CSV given employee ID"""
import csv
import requests
import sys


if __name__ == "__main__":
    API_URL = 'https://jsonplaceholder.typicode.com'
    employeeId = sys.argv[1]
    userResponse = requests.get(f'{API_URL}/users/{employeeId}')
    todosResponse = requests.get(f'{API_URL}/todos',
                                 params={"userId": employeeId})

    user = userResponse.json()
    todos = todosResponse.json()

    username = user["username"]

    with open(f"{employeeId}.csv", "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        for todo in todos:
            writer.writerow(
                [employeeId, username, str(todo["completed"]), todo["title"]]
            )
