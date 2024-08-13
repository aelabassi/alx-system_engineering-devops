#!/usr/bin/python3
""" Get the number of appearance of a keyword in a subreddit """
import requests


def count_words(subreddit, word_list, counts={}, after=None, count=0):
    """
    gets the number of appearance of a keyword in a subreddit
    Args:
        subreddit (str): subreddit to search
        word_list (list): list of keywords to search
        counts (dict): dictionary of keywords and their counts
        after (str): after token
        count (int): count of keywords found so far
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    params = {
        'limit': 100,
        'after': after,
        'count': count
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
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
    for post in posts:
        title = post['data']['title']
        for word in word_list:
            if word.lower() in title.lower().split():
                word_count = len([t for t in title.lower().split()
                                  if t == word.lower()])
                if counts.get(word) is None:
                    counts[word] = word_count
                else:
                    counts[word] += word_count
    if after is None:
        if len(counts) == 0:
            print("")
            return
        counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        [print("{}: {}".format(k, v)) for k, v in counts]
    else:
        count_words(subreddit, word_list, counts, after, count)
