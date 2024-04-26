#!/usr/bin/python3
'''
- Uses a REST API, gets information about his/her TODO progress.
- The information is then exported into a JSON file.

Usage:
    python script.py <userId>

    where <userId> is the employee's ID
'''
import json
import requests
import sys


def exports_employee_todo_progress_to_json(userId):
    '''
    exports the employee's todo progress to JSON file.

    Args:
        userId (int): user ID of the employee.

    Returns:
        None

    Prints userId, task title, task completed status, username.
    '''

    '''REST API urls given'''
    original_url = 'https://jsonplaceholder.typicode.com'
    todos_url = f"{original_url}/todos?userId={userId}"
    user_url = f"{original_url}/users/{userId}"

    '''Checking if userId provided is an integer'''
    try:
        userId = int(userId)
    except ValueError:
        print("UseId provided is not an integer")
        sys.exit(1)

    try:
        '''Using the provided REST API to gather employee information'''
        user_data = requests.get(user_url)
        user_data_json = user_data.json()
        user_name = user_data_json["username"]

        '''Getting todo list of the employees.'''
        todos_data = requests.get(todos_url)
        todos = todos_data.json()

        '''Arranging data in the required format'''
        jsn_fmt = {f'"{userId}"': []}

        for todo in todos:
            task_completed_status = (True if todo["completed"]
                                     else False)

            jsn_fmt[f'"{userId}"'].append({"task": todo["title"],
                                    "completed": task_completed_status,
                                    "username": user_name})

        ''' creating the JSON file to save in'''
        file_jsn = f"{userId}.json"
        with open(file_jsn, mode='w') as file_jsn_write:
            json.dump(jsn_fmt, file_jsn_write)

    except requests.exceptions.RequestException as e:
        print("Failed to fetch data:", e)
        sys.exit(1)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Failure!, Use python script.py <userId>")
        sys.exit(1)
    userId = int(sys.argv[1])
    exports_employee_todo_progress_to_json(userId)
