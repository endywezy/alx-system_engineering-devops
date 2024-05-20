#!/usr/bin/python3
"""
Fetch and export employee TODO list progress to a JSON file using a REST API.
"""

import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee information
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Get employee TODO list
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Extract employee name and user id
    employee_name = user_data.get("username")
    user_id = user_data.get("id")

    # Prepare the data for JSON
    tasks = [{"task": task.get("title"),
              "completed": task.get("completed"),
              "username": employee_name} for task in todos_data]

    data = {str(user_id): tasks}

    # File name
    file_name = f"{user_id}.json"

    # Write to JSON file
    with open(file_name, mode='w') as file:
        json.dump(data, file)

    print(f"Data exported to {file_name}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
