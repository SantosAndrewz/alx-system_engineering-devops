#!/usr/bin/python3
'''Uses a given REST API, returns information about his/her TODO progress.'''

import requests
import sys


def gather_employee_todo_progress(userId):
    '''
    gets the employee's todo progress using his employee ID=userId.

    Args:
        userId (int): user ID of the employee.

    Returns:
        None

    Prints employee's name, tasks completed and title, total tasks, progress.
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
        user_name = user_data_json["name"]

        '''Getting todo list of the employees.'''
        todos_data = requests.get(todos_url)
        todos = todos_data.json()

        '''Computing total tasks and tasks completed.'''
        total_tasks = len(todos)
        tasks_completed = (todo for todo in todos if todo['completed'])
        num_tasks_completed = len(tasks_completed)

        '''Computing todos progress of the employee'''
        todos_progress = (num_tasks_completed/total_tasks)

        '''Displaying todos progress'''
        print(f'Employee {user_name} is done with tasks ({todos_progress}):')

        '''Displaying the task title'''
        for task in tasks_completed:
            print(f"\t {task['title]}")

    except requests.exceptions.RequestException as e:
        print("Failed to fetch data:", e)
        sys.exit(1)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Failure!, Use python script.py <userId>")
        sys.exit(1)
    userId = int(sys.argv[1])
    gather_employee_todo_progress(userId)
