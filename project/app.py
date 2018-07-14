from flask import Flask
from flask_frozen import Freezer
from project.config import Config

app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.config.from_object(Config)
freezer = Freezer(app)