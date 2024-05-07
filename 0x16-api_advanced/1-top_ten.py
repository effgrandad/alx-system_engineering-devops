#!/usr/bin/python3
"""A program that publishes the titles of the
top 10 popular posts for a specific subreddit
after submitting a query to the Reddit API"""
import requests


def top_ten(subreddit):
    """displays the titles of the 10 initial hot posts listed"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_rdirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
