#!/usr/bin/python3
"""
Verifies that Nginx is proxying requests from port 80 to port 5000
"""
import sys

from fabric import Connection
from invoke import run
from io import StringIO
from paramiko import RSAKey
from time import sleep
import os

PASSWORD = os.getenv('PASSWORD')
host = sys.argv[1]
user = sys.argv[2]
rsa_key_file = sys.argv[3]
route = sys.argv[4]

rsa_key = RSAKey.from_private_key(open(rsa_key_file), password=PASSWORD)
output = StringIO()

def curl_server(ip, route):
    """ Sends request to student's server and returns response. """
    sleep(3)
    output = run('curl -s '+str(ip)+str(route), hide=True, warn=True)

    return output.stdout

with Connection(host, user=user, connect_kwargs={"pkey": rsa_key}) as c:
    c.run("netstat -na | grep '5000.* LISTEN'", shell="/bin/bash", out_stream=output, warn=True)
    if output.getvalue():
        print(curl_server(host, route), end="")
        exit(0)
    else:
        c.run("cd AirBnB_clone_v2 && bash -lc \"tmux new-session -d 'gunicorn --bind 0.0.0.0:5000 -p /tmp/gunginx.pid web_flask.0-hello_route:app'\"", shell="/bin/bash", out_stream=output, warn=True)
        for i in range(5):
            curl_out = curl_server(host, route)
            if curl_out == "Hello HBNB!":
                print("great")
                print(curl_out, end="")
                c.run("sudo kill -9 `cat /tmp/gunginx.pid` > /dev/null 2>&1", shell="/bin/bash", warn=True)
                exit(0)
        print(curl_out, end="")
        c.run("sudo kill -9 `cat /tmp/gunginx.pid` > /dev/null 2>&1", shell="/bin/bash", warn=True)
        exit(0)
