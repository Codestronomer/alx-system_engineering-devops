#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee
and saves to a CSV file
"""
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
    r2 = requests.get(url2).json()
    list_row = []
    for i in r2:
        list_row.append([userid, name, i.get("completed"), i.get("title")])
    filename = "{}.csv".format(userid)
    with open(filename, 'w') as file:
        writer = csv.writer(file, delimiter=",",
                            quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerows(list_row)
