#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee
and saves to a CSV file
"""
import json
import requests


if __name__ == "__main__":
    # checks if employee exists and retrieves employee name
    url1 = 'https://jsonplaceholder.typicode.com/users/'

    users = requests.get(url1).json()
    users_dict = {}
    for user in users:
        id = user.get("id")
        name = user.get("username")

        # checks for current employee todos
        url2 = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)
        r2 = requests.get(url2).json()
        list_row = []
        for i in r2:
            list_row.append({
                "username": name,
                "task": i.get("title"),
                "completed": i.get("completed"),
            })
        users_dict[id] = list_row

    filename = "todo_all_employees.json"
    with open(filename, 'w') as file:
        json.dump(users_dict, file)
