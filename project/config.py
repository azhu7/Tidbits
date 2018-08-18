"""Config objects for Flask app."""

import logging
import os

from google.cloud import datastore
from project.util import Env


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
        self.TWITTER_CONSUMER_KEY = self.get_datastore_value_(
            'TWITTER_CONSUMER_KEY')
        self.TWITTER_CONSUMER_SECRET = self.get_datastore_value_(
            'TWITTER_CONSUMER_SECRET')
        self.TWITTER_ACCESS_TOKEN = self.get_datastore_value_(
            'TWITTER_ACCESS_TOKEN')
        self.TWITTER_ACCESS_TOKEN_SECRET = self.get_datastore_value_(
            'TWITTER_ACCESS_TOKEN_SECRET')

    def get_datastore_value_(self, key):
        """Retrieves the key's value from Datastore.

        Override value by setting environment variable.

        :param key: String key
        :return String value. 'NOT_SET' if key was not found.
        """
        entity = self.client.get(self.client.key(self.entity_kind, key))
        if entity is None:
            logging.warning(
                'Key {%s} is not set in Datastore. Go to the GCP Developers '
                'Console to set it.' % key)
            value = 'NOT_SET'
        else:
            value = entity.get('value')

        env_var_override = os.environ.get(key)
        if env_var_override is not None:
            logging.info('Key {%s} overridden by environment variable.')
            value = env_var_override
        return value

    def __str__(self):
        # TODO(alexzhu): Implement this.
        return 'Not Implemented'
