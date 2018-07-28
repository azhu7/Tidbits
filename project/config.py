"""Config objects for Flask app."""

import os


class Config(object):  # pylint: disable=too-few-public-methods
    """Default Flask configuration."""
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'test-key'

    # Load API keys. Value is None if environment variable is not set.
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    TWITTER_API_KEY = os.environ.get('TWITTER_API_KEY')
