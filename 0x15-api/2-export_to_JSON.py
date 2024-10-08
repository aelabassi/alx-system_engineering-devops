#!/usr/bin/python3
"""Send request to RESTAPI
retrieve employees and tasks"""
import json
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
    with open(user_id + ".json", "w") as f:
        json.dump({user_id: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        } for task in todo]}, f)
