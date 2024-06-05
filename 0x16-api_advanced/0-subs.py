#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """ Queries the Reddit API and returns the number of subscribers """
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0
    
    data = response.json().get('data', {})
    subscribers = data.get('subscribers', 0)
    return subscribers


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the subreddit name as an argument.")
    else:
        subreddit = sys.argv[1]
        print(number_of_subscribers(subreddit))
