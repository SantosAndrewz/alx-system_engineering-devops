#!/usr/bin/python3
"""
- A module for a function that queries the Reddit API recursively.
- Parses the titles of all hot articles, prints a sorted count of given keywds
"""

import requests


def count_words(subreddit, word_list, after='', word_dict={}):
    """
    A function that queries the Reddit API and parses the title of
    all hot articles.

    Args:
        subreddit - reddit to be queried
        word_list - word list
        after - after
        word_dict - word dictionary

    Returns: -prints a sorted count of given keywords..
             -Nothing if no posts match or the subreddit is invalid.
    """

    if not word_dict:
        for w in word_list:
            if w.lower() not in word_dict:
                word_dict[w.lower()] = 0

    if after is None:
        wd = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for w in wd:
            if w[1]:
                print('{}: {}'.format(w[0], w[1]))
        return None

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    header = {'user-agent': ''Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36''}
    parameters = {'limit': 100, 'after': after}
    response = requests.get(url, headers=header, params=parameters,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        ht = response.json()['data']['children']
        afta = response.json()['data']['after']
        for pt in ht:
            t = pt['data']['title']
            l = [w.lower() for w in title.split(' ')]

            for w in word_dict.keys():
                word_dict[w] += l.count(w)

    except Exception:
        return None

    count_words(subreddit, word_list, afta, word_dict)
