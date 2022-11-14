#!/usr/bin/python3
"""
This script uses JSONplaceholder api to get employee information
"""
import requests
import sys

if __name__ == '__main__':
    # if provided with employee id
    if len(sys.argv) > 1:
        # checks if employee exists and retrieves employee name
        url1 = 'https://jsonplaceholder.typicode.com/users/{}'.format(
            sys.argv[1])
        r1 = requests.get(url1).json()
        name = r1.get("name")

        # checks for current employee todos
        url2 = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
            sys.argv[1])
        r2 = requests.get(url2).json()
        complete = [i for i in r2 if i.get("completed") == True]
        print(
            "Employee {} is done with tasks({}/{}):".format(
                name, len(complete), (len(r2)), end="")
        for i in complete:
            print("\t {}".format(i.get("title")))
