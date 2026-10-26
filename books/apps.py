# INF601 - Advanced Programming in Python
# Oumar Mballo
# Mini Project 6

"""App configuration for the books app."""

from django.apps import AppConfig


class BooksConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "books"
