#!/usr/bin/python3
"""Module to export TODO lists from API in JSON"""
import json
import requests
import sys


if __name__ == "__main__":
    API_URL = 'https://jsonplaceholder.typicode.com'

    userResponse = requests.get(f'{API_URL}/users')
    users = userResponse.json()

    todos_json = dict()

    for user in users:
        userId = user["id"]
        todosResponse = requests.get(f'{API_URL}/todos',
                                     params={"userId": userId})
        todos = todosResponse.json()
        todos_list = []

        for todo in todos:
            todo_dict = {
                "task": todo["title"],
                "completed": todo["completed"],
                "username": user["username"]
            }
            todos_list.append(todo_dict)

        todos_json[userId] = todos_list

    with open('todo_all_employees.json', 'w', encoding='utf-8') as file:
        json.dump(todos_json, file)
