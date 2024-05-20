#!/usr/bin/python3
"""
Fetches to-do lists users from a REST API and saves them to a JSON file.
"""

import json
import requests

# API endpoints
API_TODOS = 'https://jsonplaceholder.typicode.com/todos'
API_USERS = 'https://jsonplaceholder.typicode.com/users'


def fetch_data(url):
    """
    Fetches data from the given URL.
    """
    response = requests.get(url)
    return response.json()


def main():
    """
    Main function to fetch data and export to JSON.
    """
    users = fetch_data(API_USERS)
    todos = fetch_data(API_TODOS)

    user_dict = {}
    for user in users:
        user_id = user['id']
        user_dict[user_id] = []

    for todo in todos:
        user_id = todo['userId']
        task_dict = {
            "username": next(user['username'] for user in users
                             if user['id'] == user_id),
            "task": todo['title'],
            "completed": todo['completed']
        }
        user_dict[user_id].append(task_dict)

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(user_dict, json_file)


if __name__ == "__main__":
    main()
