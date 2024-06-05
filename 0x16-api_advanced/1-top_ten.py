#!/usr/bin/python3
'''
  this module contains the function top_ten
'''
import requests
from sys import argv


def top_ten(subreddit):
  '''
    returns the top ten posts for a given subreddit
  '''
  user = {'User-Agent': 'Lizzie'}
  url = requests.get('https://www.reddit.com/r/{}/hot/.json?limit=10'
                     .format(subreddit), headers=user).json()

  # Check if 'data' and 'children' exist before accessing them
  if url.get('data') is not None and url['data'].get('children') is not None:
    for post in url['data']['children']:
      print(post['data'].get('title'))
  else:
    print("Error: Unable to retrieve data from Reddit")


if __name__ == "__main__":
  # Check if there's a subreddit argument provided
  if len(argv) < 2:
    print("Usage: ./1-top_ten.py <subreddit>")
    exit(1)

  top_ten(argv[1])
