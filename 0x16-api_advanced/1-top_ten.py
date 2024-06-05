#!/usr/bin/python3
"""
    This module contains the function top_ten
"""

import requests
from sys import argv


def top_ten(subreddit):
    """
        Returns the top ten posts for a given subreddit
    """
    user = {'User-Agent': 'Lizzie'}
    url = 'https://www.reddit.com/r/{}/hot/.json?limit=10'.format(subreddit)
    response = requests.get(url, headers=user)

    if response.status_code != 200:
        print(None)
        return

    data = response.json()
    try:
        for post in data.get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)


if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: {} <subreddit>".format(argv[0]))
    else:
        top_ten(argv[1])
