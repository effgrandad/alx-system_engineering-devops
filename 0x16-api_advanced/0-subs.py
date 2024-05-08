#!/usr/bin/python3
"""A feature that retrieves the quantity of
subscribes from the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subcribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0. (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
