"""Query class."""

import tweepy
from flask import current_app as app

class Query(object):  # pylint: disable=too-few-public-methods
    """Class to query multiple API's."""
    def __init__(self):
        # Authenticates multiple API's

        # Twitter authentification process
        twitter_auth = tweepy.OAuthHandler(app.config['TWIT_CONSUMER_KEY'],
                                           app.config['TWIT_CONSUMER_SECRET'])
        twitter_auth.set_access_token(app.config['TWIT_ACCESS_TOKEN'],
                                      app.config['TWIT_ACCESS_TOKEN_SECRET'])
        self.twitter_api = tweepy.API(twitter_auth)


    def twitter_search(self, query, num=100):
        """Given a query and optional number of tweets to return,
        returns a list of tweet messages received from the Twitter API.
        """
        search = self.twitter_api.search(q=query, lang='en', count=str(num),
                                         tweet_mode='extended')
        return [item.full_text for item in search]


    def query(self, query):
        """Given a query, accesses multiple API's with that query and returns
        a dictionary with the key being the API accessed, and the value
        being a list of text returned from the API.

        Example return object: {'twitter': [tweet1, tweet2, ...]}
        """
        response = {}
        response['twitter'] = self.twitter_search(query)
        # Insert other API calls here.
        return response
