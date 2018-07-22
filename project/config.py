"""Config objects for Flask app."""

import os


class Config(object):  # pylint: disable=too-few-public-methods
    """Default Flask configuration."""
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'test-key'
