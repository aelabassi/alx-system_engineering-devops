#!/usr/bin/python3
""" top 10 hot posts in a subreddit """
import requests


def top_ten(subreddit):
    """
    gets the top 10 hot posts in a subreddit
    Args:
        subreddit (str): subreddit to search
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print("None")
    data = response.json()
    posts = data['data']['children']
    for post in posts:
        print(post['data']['title'])
