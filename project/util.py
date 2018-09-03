"""Utility for Tidbits."""
from enum import Enum, auto
import os


class Env(Enum):
    PROD = auto()
    DEV = auto()


def get_env():
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        return Env.PROD
    else:
        return Env.DEV
