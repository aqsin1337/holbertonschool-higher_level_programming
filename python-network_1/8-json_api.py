#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a letter"""
import sys
import requests

if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}
    url = "http://0.0.0.0:5000/search_user"
    headers = {'cfclearance': 'true'}

    r = requests.post(url, data=payload, headers=headers)
    try:
        response = r.json()
        if not response:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
