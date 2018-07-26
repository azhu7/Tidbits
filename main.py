#!/usr/bin/python3
"""Main. Run this file to start the server."""

import json
import logging.config
import os

from project.app import app as application  # gunicorn looks for 'application'.
import project.views  # Make sure Flask loads all endpoints. pylint: disable=unused-import

_PORT = int(os.environ.get('PORT', 5000))


def init_logging(default_level=logging.INFO):
    """Loads the logging config if present or uses default settings."""
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        # App is running in production environment.
        config_path = 'logging_prod.json'
    else:
        # App is running in dev environment.
        config_path = 'logging_dev.json'
        log_dir = '.logs/'
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)  # Must create dir as it is used in logging.json.

    if os.path.exists(config_path):
        with open(config_path, 'rt') as config_file:
            config = json.load(config_file)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
    logging.info('Successfully initialized logger.')


def main():
    """Runs initialization and server."""
    init_logging()
    logging.info('Starting app.')
    application.run(host='0.0.0.0', port=_PORT)


if __name__ == '__main__':
    main()
