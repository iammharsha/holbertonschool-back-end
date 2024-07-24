#!/usr/bin/python3
"""Module to fetch TODO list from API given employee ID"""
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

    totalTask = len(todos)
    completedTask = [todo for todo in todos if todo['completed']]
    totalCompletedTask = len(completedTask)

    print(f'Employee {user["name"]} is done with tasks'
          f'({totalCompletedTask}/{totalTask}):')
    for task in completedTask:
        print(f'\t {task["title"]}')
