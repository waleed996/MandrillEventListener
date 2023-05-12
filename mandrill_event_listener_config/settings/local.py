"""Set local environment settings/variables"""

from .dev import *

DEBUG = True
SQLALCHEMY_ECHO = True

# Channel layer config
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}

# Local Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'mandrill_event_listener_db.sqlite3',
    }
}
