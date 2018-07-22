"""Flask app setup."""

from flask import Flask

from project.config import Config

app = Flask(__name__)  # pylint: disable=invalid-name
app.config.from_object(Config)
