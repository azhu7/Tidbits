"""Config objects for Flask app."""

import logging

from google.cloud import datastore
from project.util import Env

NOT_SET_ = 'NOT_SET'


class Config(object):  # pylint: disable=too-few-public-methods
    """Default Flask configuration."""
    def __init__(self, env):
        """Sets app keys depending on what environment the app is running in."""
        self.client = datastore.Client()
        if env == Env.PROD:
            self.entity_kind = 'Settings_prod'
        else:
            self.entity_kind = 'Settings_dev'

        self.DEBUG = True
        # Token for CSRF protection.
        self.SECRET_KEY = self.get_datastore_value_('CSRF_PROTECTION_KEY')
        # News API
        self.NEWS_API_KEY = self.get_datastore_value_('NEWS_API_KEY')
        # Twitter API
        self.TWITTER_CONSUMER_KEY = self.get_datastore_value_('TWITTER_CONSUMER_KEY')
        self.TWITTER_CONSUMER_SECRET = self.get_datastore_value_('TWITTER_CONSUMER_SECRET')
        self.TWITTER_ACCESS_TOKEN = self.get_datastore_value_('TWITTER_ACCESS_TOKEN')
        self.TWITTER_ACCESS_TOKEN_SECRET = self.get_datastore_value_('TWITTER_ACCESS_TOKEN_SECRET')

    def get_datastore_value_(self, key):
        """Retrieves the key's value from Datastore.

        :param key: String key
        :return String value. NOT_SET_ if key was not found.
        """
        entity = self.client.get(self.client.key(self.entity_kind, key))
        if entity is None:
            logging.warning('Key {%s} is not set.' % key)
            return NOT_SET_
        else:
            return entity.get('value')

    def __str__(self):
        return 'Not Implemented'
