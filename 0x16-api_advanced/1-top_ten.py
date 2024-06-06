#!/usr/bin/python3

"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""

import requests
import sys


def top_ten(subreddit):
    """
    Queries the Reddit API for the top ten hot posts of a subreddit
    Args:
        subreddit (str): The name of the subreddit to query

    Returns:
        None
    """
    user_agent = 'Mozilla/5.0'  # Updated user agent

    headers = {
        'User-Agent': user_agent
    }

    params = {
        'limit': 10
    }

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        print(f"Error: Could not retrieve data. Status code: {response.status_code}")
        return

    try:
        data = response.json().get('data', {}).get('children', [])
    except ValueError:
        print("Error: Invalid JSON format in response")
        return

    if not data:
        print(f"No hot posts found in subreddit: {subreddit}")
        return

    for post in data:
        print(post['data']['title'])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./10-top_ten.py <subreddit>")
        sys.exit(1)

    subreddit = sys.argv[1]
    top_ten(subreddit)
