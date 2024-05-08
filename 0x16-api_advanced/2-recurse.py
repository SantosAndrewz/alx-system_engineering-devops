#!/usr/bin/python3
"""
module for recursively queriying Reddit API.
Returns a list of the titles for all hot articles for given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Function for recursively queriying Reddit API.

    Args:
        subreddit (str): the subreddit to be queried.

    Returns: a list of titles of all hot posts on a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "my_user)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    dat = response.json().get("data")
    after = dat.get("after")
    count += dat.get("dist")
    for d in dat.get("children"):
        hot_list.append(d.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
