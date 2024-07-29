#!/usr/bin/python3
"""Send request ton RESTAPI
retrieve employees and tasks"""
import json
import requests

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "User-Agent": "Holberton School"
}

base_url = "https://jsonplaceholder.typicode.com/users/"

if __name__ == "__main__":
    users = requests.get(base_url).json()
    with open("todo_all_employees.json", "w") as f:
        json.dump({
            str(user.get("id")): [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user.get("username")
            } for task in requests.get(base_url +
                                       str(user.get("id")) + "/todos",
                                       headers=headers).json()]
            for user in users
        }, f)
