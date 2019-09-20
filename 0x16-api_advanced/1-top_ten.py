#!/usr/bin/python3
"""prints the titles of the first 10 hot posts listed for a given subreddit."""

import requests


def top_ten(subreddit):
    usr = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'}
    url = requests.get('https://www.reddit.com/r/{}/about.json'.format
                       (subreddit), allow_redirects=False)
    u = url.json()
    for i in range(10):
        try:
            print(('data')('children')[i]['data']['title'])
        except Exception:
            print(None)
