import frappe
import tweepy
from . import credential
import requests
from requests_oauthlib import OAuth1

def test(doc, method=None):
    # Set up the OAuth1 object for authentication
    auth = OAuth1(credential.api_key, credential.api_key_secret, credential.access_token, credential.access_token_secrets)

    # Define the tweet content
    tweet = {"text": "Hello, World! This is a tweet sent via OAuth 1.0."}

    # Twitter API v2 endpoint to post a tweet
    url = "https://api.twitter.com/2/tweets"

    # Send a POST request to the Twitter API
    response = requests.post(url, auth=auth, json=tweet)  # Use 'json' instead of 'data'

    # Check the response from Twitter
    if response.status_code == 201:  # 201 is the success code for resource creation
        frappe.log_error("Tweet posted successfully!")
    else:
        frappe.log_error(f"Failed to post tweet. Status code: {response.status_code}, Response: {response.text}")
