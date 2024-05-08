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

    if not  isinstance(subreddit, str) or not subreddit:
        return 0

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    usr_header = {"User-Agent": "Mozilla/5.0"}
    rsp = requests.get(url, headers=usr_header, allow_redirects=False).json()

    if rsp.ok:
        try:
            rsp_data = rsp.json()
            return rsp_data.get("data", {}).get("subscribers", 0)
        except ValueError as e:
            print(f"Error decoding JSON response: {e}")
            print(f"Response text: {rsp.text}")
            return 0
    else:
        print(f"Request failed with status code {response.status_code}")
        print(f"Response text: {rsp.text}")
        return 0
