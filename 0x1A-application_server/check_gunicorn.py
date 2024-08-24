#!/usr/bin/python3
"""
Verifies that a student created the appropriate file.
"""
import sys

from fabric import Connection
from flask.cli import shell_command
from invoke import run
from io import StringIO
from paramiko import RSAKey
from time import sleep
import os

host = sys.argv[1]
user = sys.argv[2]
rsa_key_file = sys.argv[3]
route = sys.argv[4]
PASSWORD = os.getenv("PASSWORD")

rsa_key = RSAKey.from_private_key(open(rsa_key_file), password=PASSWORD)
output = StringIO()

with Connection(host, user=user, connect_kwargs={"pkey": rsa_key}) as c:
    c.run("netstat -na | grep '6000.* LISTEN'", shell="/bin/bash", out_stream=output, warn=True)
    if output.getvalue():
        curl_output = StringIO()
        print("it's running")
        c.run(command="curl -s 127.0.0.1:6000{}".format(route), shell="/bin/bash", out_stream=curl_output, warn=True)
        print(curl_output.getvalue(), end="")
        exit(0)
    else:
        # just checking if we're in the right directory
        ls_out =  StringIO()
        c.run(command="ls ./", shell="/bin/bash", out_stream=ls_out, warn=True)
        if "AirBnB_clone_v2" not in ls_out.getvalue():
            print("Directory not found")
            exit(0)

        c.run("cd AirBnB_clone_v2 ; bash -lc \"tmux new-session -d 'gunicorn --bind 0.0.0.0:6000 -p /tmp/gun.pid web_flask.0-hello_route:app'\"", shell="/bin/bash", warn=True)
        for i in range(5):
            curl_output = StringIO()
            sleep(3)
            c.run("curl -s 127.0.0.1:6000{}".format(route), shell="/bin/bash", out_stream=curl_output, warn=True)
            if curl_output.getvalue() == "Hello HBNB!":
                print("great")
                print(curl_output.getvalue(), end="")
                c.run("sudo kill -9 `cat /tmp/gun.pid` > /dev/null 2>&1")
                exit(0)
        print(route)
        print(curl_output.getvalue(), end="")
        #c.run("sudo kill -9 `cat /tmp/gun.pid` > /dev/null 2>&1")
        exit(0)
