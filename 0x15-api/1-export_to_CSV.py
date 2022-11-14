#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import csv
import requests
import sys


if __name__ == "__main__":
    # checks if employee exists and retrieves employee name
    url1 = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        sys.argv[1])
    r1 = requests.get(url1).json()
    name = r1.get("username")

    # checks for current employee todos
    url2 = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        sys.argv[1])
    r2 = requests.get(url2).json()
    filename = "{}.csv".format(sys.argv[1])
    with open(filename, 'w') as file:
        writer = csv.writer(file, delimiter=",",
                            quotechar='"', quoting=csv.QUOTE_ALL)
        for i in r2:
            row = [sys.argv[1], name]
            row.append(i.get("completed"))
            row.append(i.get("title"))
            writer.writerow(row)
