#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import csv
import requests
import sys


if __name__ == "__main__":
    userid = sys.argv[1]
    # checks if employee exists and retrieves employee name
    url1 = 'https://jsonplaceholder.typicode.com/users/{}'.format(userid)
    r1 = requests.get(url1).json()
    name = r1.get("username")

    # checks for current employee todos
    url2 = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(userid)
    tasks = requests.get(url2).json()

    # save to csv
    attrs = ["userId", "username", "completed", "title"]
    with open("{}.csv".format(id), "w") as f:
        employee_writer = csv.DictWriter(
            f, fieldnames=attrs, quoting=csv.QUOTE_ALL)
        for task in tasks:
            if task.get("userId") == id:
                task["username"] = name
                del task['id']
                employee_writer.writerow(task)
