#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
the top ten hot posts of a subreddit
"""
import requests
import sys


def top_ten(subreddit):
    """ Queries to Reddit API """
    u_agent = 'Chrome/106.0'

    headers = {
        'User-Agent': u_agent
    }

    params = {
        'limit': 10
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)
    try:
        res.raise_for_status()  # Raise an exception for HTTP errors
        dic = res.json()
        hot_posts = dic['data']['children']

        if not hot_posts:
            print("No hot posts found in subreddit: {}".format(subreddit))
            return

        for post in hot_posts:
            print(post['data']['title'])

    except requests.HTTPError as e:
        print("Error: HTTP request failed:", e)

    except requests.exceptions.RequestException as e:
        print("Error: Request failed:", e)

    except ValueError:
        print("Error: Invalid JSON format in response")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
