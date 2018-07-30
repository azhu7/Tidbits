"""Twitter API"""

import tweepy
import project.api_config # if error, read the docstring in api_config_example


class TwitterQuery():
    """Class to access Twitter API."""
    def __init__(self):
        # Authentification process
        twitter_config = project.api_config.TWITTER_CONFIG
        try:
            auth = tweepy.OAuthHandler(twitter_config['consumer_key'], twitter_config['consumer_secret'])
            auth.set_access_token(twitter_config['access_token'], twitter_config['access_token_secret'])
            self.api = tweepy.API(auth)
            print "Success authentification!"
        except:
            print "Authentification failed"

    def search(self, query):
        # Given a query, returns a list of tweet messages returned from the Twitter API
        search = self.api.search(q=query, lang='en', count='100', tweet_mode='extended')
        tweet_messages = []
        for item in search:
            tweet_messages.append(item.full_text)
        return tweet_messages
