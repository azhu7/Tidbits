'''Entry point to all things to avoid circular imports.'''
from project.app import app, freezer
from project.views import *