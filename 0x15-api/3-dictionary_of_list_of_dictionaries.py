import json
import requests


def fetch_data(url):
    response = requests.get(url)
    return response.json()


def fetch_users_tasks():
    users = fetch_data('https://jsonplaceholder.typicode.com/users')
    todos = fetch_data('https://jsonplaceholder.typicode.com/todos')

    all_tasks = {}

    for user in users:
        user_id = user['id']
        username = user['username']
        user_tasks = []

        for task in todos:
            if task['userId'] == user_id:
                task_info = {
                    "username": username,
                    "task": task['title'],
                    "completed": task['completed']
                }
                user_tasks.append(task_info)

        all_tasks[user_id] = user_tasks

    return all_tasks


def save_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)


if __name__ == "__main__":
    data = fetch_users_tasks()
    save_to_json(data, 'todo_all_employees.json')
