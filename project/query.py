"""Query class."""

import os
import tweepy

class Query(object): # pylint: disable=too-few-public-methods
    """Class to query multiple API's."""
    def __init__(self):
        # Authenticates multiple API's

        # Twitter authentification process
        twit_consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
        twit_consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
        twit_access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
        twit_access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
        twitter_auth = tweepy.OAuthHandler(twit_consumer_key,
                                           twit_consumer_secret)
        twitter_auth.set_access_token(twit_access_token,
                                      twit_access_token_secret)
        self.twitter_api = tweepy.API(twitter_auth)


    def twitter_search(self, query, num=100):
        """ Given a query and optional number of tweets to return,
        returns a list of tweet messages
        received from the Twitter API
        """
        search = self.twitter_api.search(q=query, lang='en', count=str(num),
                                         tweet_mode='extended')
        tweet_messages = []
        for item in search:
            tweet_messages.append(item.full_text)
        return tweet_messages
