#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee
and saves to a CSV file
"""
import json
import requests
import sys


if __name__ == "__main__":
    userid = sys.argv[1]
    # checks if employee exists and retrieves employee name
    url1 = 'https://jsonplaceholder.typicode.com/users/'.format(userid)
    r1 = requests.get(url1).json()
    name = r1.get("username")

    # checks for current employee todos
    url2 = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(userid)
    r2 = requests.get(url2).json()
    list_row = []
    for i in r2:
        list_row.append({"task": i.get("title"),
                         "completed": i.get("completed"),
                         "username": name})
    employee_dict = {userid: list_row}

    filename = "{}.json".format(userid)
    with open(filename, 'w') as file:
        json.dump(employee_dict, file)
