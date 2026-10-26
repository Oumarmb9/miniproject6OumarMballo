# INF601 - Advanced Programming in Python
# Oumar Mballo
# Mini Project 6

"""ASGI config for the BookNook project."""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "booknook.settings")

application = get_asgi_application()
