#!/usr/bin/python3
"""
This script uses JSONplaceholder api to get employee information
"""
import sys
import requests

if __name__ == '__main__':
    # if provided with employee id
    if len(sys.argv) > 1:
        # checks if employee exists and retrieves employee name
        url1 = 'https://jsonplaceholder.typicode.com/users/{}'.format(
            sys.argv[1])
        r1 = requests.get(url1).json()
        name = r1["name"]

        # checks for current employee todos
        url2 = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
            sys.argv[1])
        r2 = requests.get(url2).json()
        complete = [i for i in r2 if i["completed"] == True]
        print(
            f"Employee {name} is done with tasks({len(complete)}/{len(r2)}):")
        for i in complete:
            print("\t {}".format(i["title"]))
