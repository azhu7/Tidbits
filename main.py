from project.app import app
from project.views import *  # Ensure all routes are registered before app.run.

import os
import logging
from logging import config
import json

LOG_DIR = '.logs/'
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)


def init_logging(config_path='logging.json', default_level=logging.INFO):
    if os.path.exists(config_path):
        with open(config_path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


if __name__ == '__main__':
    init_logging()
    port = int(os.environ.get('PORT', 5000))
    logging.info('Starting app.')
    app.run(host='0.0.0.0', port=port)
