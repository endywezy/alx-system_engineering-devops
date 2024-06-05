#!/usr/bin/python3
"""
This module contains the function number_of_subscribers.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit. If an invalid subreddit is given,
    returns 0.
    
    Args:
        subreddit (str): The name of the subreddit.
    
    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    user_agent = {'User-Agent': 'MyUserAgent'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    
    try:
        response = requests.get(url, headers=user_agent, allow_redirects=False)
        if response.status_code != 200:
            return 0
        
        data = response.json()
        return data['data']['subscribers']
    except Exception:
        return 0
