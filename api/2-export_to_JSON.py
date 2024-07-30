#!/usr/bin/python3
"""Module to export TODO list from API in JSON given employee ID"""
import json
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

    todos_json = {employeeId: []}
    for todo in todos:
        todo_dict = {
            "task": todo["title"],
            "completed": todo["completed"],
            "username": username
        }
        todos_json[employeeId].append(todo_dict)

    with open(f"{employeeId}.json", 'w', encoding='utf-8') as file:
        json.dump(todos_json, file)
