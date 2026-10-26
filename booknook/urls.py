# INF601 - Advanced Programming in Python
# Oumar Mballo
# Mini Project 6

"""Top-level URL configuration for the BookNook project."""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # Django's built-in auth views (login, logout, password reset, ...).
    path("accounts/", include("django.contrib.auth.urls")),
    # Our app's URLs, including a custom register view.
    path("", include("books.urls")),
]
