"""Config objects for Flask app."""

from google.cloud import datastore
from project.util import Env


class Config(object):  # pylint: disable=too-few-public-methods
    """Default Flask configuration."""

    def __init__(self, env):
        client = datastore.Client()
        if env == Env.PROD:
            entity_kind = 'Settings_prod'
        else:
            entity_kind = 'Settings_dev'

        self.DEBUG = True

        # Token for CSRF protection.
        self.SECRET_KEY = client.get(
            client.key(entity_kind, 'CSRF_PROTECTION_KEY')).get('key') or 'test-key'
        self.TWITTER_API_KEY = client.get(
            client.key(entity_kind, 'TWITTER_API_KEY')).get('key') or 'test-key'
