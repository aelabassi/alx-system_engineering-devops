#!/usr/bin/python3
"""Send request ton RESTAPI
retrieve employees and tasks"""
import requests
import sys

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "User-Agent": "Holberton School"
}

base_url = "https://jsonplaceholder.typicode.com/users/"

if __name__ == "__main__":
    user_id = sys.argv[1]
    user = requests.get(base_url + user_id).json()
    todo = requests.get(base_url + user_id + "/todos/", headers=headers).json()
    done = [task for task in todo if task.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done), len(todo)))
    [print("\t {}".format(task.get("title"))) for task in done]
