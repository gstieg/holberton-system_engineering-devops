#!/usr/bin/python3
""" Reddit API and returns the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """count of how many subscribers"""

    usr = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'}
    url = requests.get('https://www.reddit.com/r/{}/about.json'.format
                       (subreddit), allow_redirects=False)

    try:
        return url.json()['data']['subscribers']
    except Exception:
        return 0
