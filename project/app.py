from flask import Flask
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from project.config import Config

app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.config.from_object(Config)
pages = FlatPages(app)
freezer = Freezer(app)