#!/usr/bin/python3
"""A program that publishes the titles of the
top 10 popular posts for a specific subreddit
after submitting a query to the Reddit API"""

import requests
from sys import atgv

def top_ten(subreddit):
    """displays the titles of the 10 initial hot posts listed"""
    user = {'User-Agent': 'Lizzie'}
    url = requests.get('https://www.reddit.com/r/{}/hot/.json?limit=10'
                       .format(subreddit), headers=user).json()
    try:
        for post in url.get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)


if __name__ == "__main__":
    top_ten(argv[1])
