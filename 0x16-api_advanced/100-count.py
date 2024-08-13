#!/usr/bin/python3
""" Get the number of appearence of a keyword in a subreddit """
import requests


def count_words(subreddit, word_list, counts={}, after=None, count=0):
    """ gets the number of appearence of a keyword in a subreddit """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    params = {
        'limit': 100,
        'after': after,
        'count': count
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    try:
        result = response.json()
        if response.status_code != 200:
            raise Exception
    except Exception:
        print("")
        return
    data = result.get("data")
    after = data['after']
    count += data['dist']
    posts = data['children']
    for word in word_list:
        counts[word] = 0
    for post in posts:
        title = post['data']['title']
        for word in word_list:
            if word.lower() in title.lower().split():
                counts[word] += title.lower().split().count(word.lower())
    if after is None:
        counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        [print("{}: {}".format(k, v)) for k, v in counts]
    else:
        count_words(subreddit, word_list, after, count)
