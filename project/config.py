"""Config objects for Flask app."""

import os


class Config(object):  # pylint: disable=too-few-public-methods
    """Default Flask configuration."""
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'test-key'
    API_KEY = '8661aeb44b0c45b29962447873da64db'
