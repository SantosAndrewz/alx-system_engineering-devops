#!/usr/bin/python3
"""
A module on querying the Reddit API to return the number of subscribers.

Return: Number of of subscribers for a given valid subreddit else 0.
"""

import requests
import time


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers.

    Args:
        subreddit (str): The name of the subreddit to be queried.

    Returns:
        int: Number of of subscribers if subreddit valid else 0.
    """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y;\
rv:42.0) Gecko/20100101 Firefox/42.0"}

    try:
        rsp = requests.get(url, headers=headers, allow_redirects=False)
        print(rsp)

        if rsp.status_code == 200:
            rsp_data = rsp.json()
            return rsp_data.get("data").get("subscribers")
        else:
            return 0

    except Exception as e:

        print(f"An error occurred: {str(e)}")

    time.sleep(4)
