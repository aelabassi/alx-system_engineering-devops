#!/usr/bin/python3
""" Get all hot posts in a subreddit """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ gets all hot posts in a subreddit """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    params = {
        'limit': 100,
        'after': after
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json()
    posts = data['data']['children']
    for post in posts:
        hot_list.append(post['data']['title'])
    after = data['data']['after']
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
