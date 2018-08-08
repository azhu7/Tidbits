"""Config objects for Flask app."""

import os


class Config(object):  # pylint: disable=too-few-public-methods
    """Default Flask configuration."""
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'test-key'
    TWIT_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
    TWIT_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
    TWIT_ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN')
    TWIT_ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
