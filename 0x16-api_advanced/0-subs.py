#!/usr/bin/python3
"""
A module on querying the Reddit API to return the number of subscribers.

Return: Number of of subscribers for a given valid subreddit else 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers.

    Args:
        subreddit (str): The name of the subreddit to be queried.

    Returns:
        int: Number of of subscribers if subreddit valid else 0.
    """

    url = f'https://www.reddit.com/r/subreddit/about.json'
    headers = {"User-Agent": "My_user"}
    rsp = requests.get(url, headers=headers, allow_redirects=False)

    if rsp.ok:
        print(rsp)
        rsp_data = rsp.json()
        print(rep_data)
        return rsp_data.get("data").get("subscribers")
    else:
        return 0
