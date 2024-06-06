#!/usr/bin/python3
"""
Module to fetch top ten posts from a subreddit using the Reddit API.
"""

import requests


def top_ten(subreddit):
    """
    Fetches and prints the top ten posts from the specified subreddit.

    Args:
        subreddit (str): The name of the subreddit to fetch posts from.
    """
    url = (
        "https://www.reddit.com/r/" +
        subreddit +
        "/hot.json?limit=10"
    )
    headers = {"User-Agent": "MyAPIAgent"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                print(post['data']['title'])
    else:
        print(None)


if __name__ == "__main__":
    top_ten("programming") 
