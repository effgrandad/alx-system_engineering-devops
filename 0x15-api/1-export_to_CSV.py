#!/usr/bin/python3
"""exports to-do list data in CSV format for specified employee ID"""

import csv
import requests
import sys

if __name__ == "__name__":
    user = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, task.get("completed"), task.get("title")]
         ) for task in todos]
