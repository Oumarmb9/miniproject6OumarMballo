# INF601 - Advanced Programming in Python
# Oumar Mballo
# Mini Project 6

"""WSGI config for the BookNook project."""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "booknook.settings")

application = get_wsgi_application()
