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

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    usr_header = {"User-Agent": "My_user"}
    rsp = requests.get(url, headers=usr_header, allow_redirects=False)

    if rsp.ok:
        rsp_data = rsp.json()
        return rsp_data.get("data").get("subscribers")
    else:
        return 0
