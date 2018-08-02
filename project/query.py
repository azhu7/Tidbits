"""Query class."""

import tweepy
import project.api_config # if error, read the docstring in api_config_example


class Query(object): # pylint: disable=too-few-public-methods
    """Class to query multiple API's."""
    def __init__(self):
        # Authenticates multiple API's

        # Twitter authentification process
        twitter_config = project.api_config.TWITTER_CONFIG
        twitter_auth = tweepy.OAuthHandler(twitter_config['consumer_key'],
                                           twitter_config['consumer_secret'])
        twitter_auth.set_access_token(twitter_config['access_token'],
                                      twitter_config['access_token_secret'])
        self.twitter_api = tweepy.API(twitter_auth)


    def twitter_search(self, query):
        """ Given a query, returns a list of tweet messages
        returned from the Twitter API
        """
        search = self.twitter_api.search(q=query, lang='en', count='100',
                                         tweet_mode='extended')
        tweet_messages = []
        for item in search:
            tweet_messages.append(item.full_text)
        return tweet_messages
