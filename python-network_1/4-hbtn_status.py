#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""
import requests

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    headers = {'cfclearance': 'true'}
    r = requests.get(url, headers=headers)
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
