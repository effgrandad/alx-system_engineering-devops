#!/usr/bin/python3
"""
Script to print hot posts on a given Reddit subreddit.
"""

import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # set headers for the HTTP request, including that of User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
	
    }

    # Set parameters for the request, limiting the number of posts to 10 
    params = {
        "limit": 10
    }

    # send a GET request to access the subreddit's hot posts page
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    # Verify whether a not-found error (404) is indicated by the response status code.
    if response.status_code == 404:
        print("None")
        return

    results = response.json().get("data")
    # print titles of the top 10 hottest posts
    [print(c.get("data").get("title")) for c in results.get("children")]
