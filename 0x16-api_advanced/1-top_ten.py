#!/usr/bin/python3
"""
Module for uring the Reddit API to print titles of first 10 hot posts.
Returns titles of first 10 hot posts for valid subreddits else none.
"""

import requests


def top_ten(subreddit):
    """
    Function queries the Reddit API to print titles of first 10 hot posts.

    Args:
        subreddit (str): The name of the subreddit to be queried.

    Returns:
        str: top 10 hot posts listed for a given subreddit.
    """
    rq = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "my_agent"},
        params={"limit": 10}

    )

    if rq.status_code == 200:
        for dat in rq.json().get("data").get("children"):
            title = dat.get("data").get("title")
            print(title)
    else:
        print(None)
