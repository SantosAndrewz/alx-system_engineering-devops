#!/usr/bin/python3
'''
- Uses a REST API, gets information about his/her TODO progress.
- The information is then exported into a csv file.

Usage:
    python script.py <userId>

    where <userId> is the employee's ID
'''
import csv
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
        user_name = user_data_json["username"]

        '''Getting todo list of the employees.'''
        todos_data = requests.get(todos_url)
        todos = todos_data.json()

        '''creating the CSV file to save in.'''
        file_csv = f"{userId}.csv"
        with open(file_csv, mode='w', newline='') as file_csv_write:
            file_csv_writer = csv.writer(file_csv_write, quoting=csv.QUOTE_ALL)

            '''exporting the data into the CSV and display of progress'''
            for todo in todos:
                task_completed_status = ("True" if todo["completed"]
                                         else "False")
                file_csv_writer.writerow([userId, user_name,
                                         task_completed_status, todo["title"]])

    except requests.exceptions.RequestException as e:
        print("Failed to fetch data:", e)
        sys.exit(1)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Failure!, Use python script.py <userId>")
        sys.exit(1)
    userId = int(sys.argv[1])
    gather_employee_todo_progress(userId)
