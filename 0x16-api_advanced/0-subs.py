#!/usr/bin/python3
""" Get the number of subscribers in a subreddit """
import requests


def number_of_subscribers(subreddit):
    """ gets the number of sub scribers in a subreddit """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json()
    return data['data']['subscribers']
