#!/usr/bin/python3
"""
Script to query a list of all hot posts on a given Reddit subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Recursively retrieves a list of titles of all hot posts
    on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list, optional): List to store the post titles.
                                    Default is an empty list.
        after (str, optional): Token used for pagination.
                                Default is an empty string.
        count (int, optional): Current count of retrieved posts. Default is 0.

    Returns:
        list: A list of post titles from the hot section of the subreddit.
    """
    # Create the URL for the subreddit's hot posts in JSON format
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # Define headers for the HTTP request, including User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Establish the request's parameters, such as pagination and limit
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    # Making GET call to hot posts page of the subreddit.
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Verify if the response status code indicates a not-found error (404)
    if response.status_code == 404:
        return None
    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")

    # Add the post names to the hot_list.
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    # Call the procedure recursively if additional posts are to be retrieved.
    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    # Print final list of hot post titles
    return hot_list
