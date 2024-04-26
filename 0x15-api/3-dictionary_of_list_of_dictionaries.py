#!/usr/bin/python3
'''
- Uses a REST API, gets information about their TODO progress.
- The information is then exported into a JSON file.

Usage:
    python script.py
'''
import json
import requests
import sys


def exports_employees_todo_progress_to_json():
    '''
    exports the employees' todo progress to JSON file.

    Returns:
        None

    Prints userId, username, task title, task completed status.
    '''

    '''REST API urls given'''
    original_url = 'https://jsonplaceholder.typicode.com'
    users_url = f"{original_url}/users"

    ''' Initializing jsn_fmt'''
    jsn_fmt = {}

    try:
        '''Using the provided REST API to gather employee information'''
        users_data = requests.get(users_url)
        users_jsn = users_data.json()

        for user in users_jsn:
            userId = user["id"]
            user_name = user["username"]

            '''Getting todo list of the employees.'''
            todos_url = f"{original_url}/todos?userId={userId}"
            todos_data = requests.get(todos_url)
            todos = todos_data.json()

            '''Arranging data in the required format'''
            jsn_fmt[str(userId)] = []
            for todo in todos:
                task_completed_status = (True if todo["completed"]
                                         else False)

                jsn_fmt[f'{userId}'].append({"username": user_name, "task":
                                             todo["title"], "completed":
                                             task_completed_status})

        ''' creating the JSON file to save in'''
        file_jsn = f"todo_all_employees.json"
        with open(file_jsn, mode='w') as file_jsn_write:
            json.dump(jsn_fmt, file_jsn_write)

    except requests.exceptions.RequestException as e:
        print("Failed to fetch data:", e)
        sys.exit(1)


if __name__ == "__main__":

    exports_employees_todo_progress_to_json()
