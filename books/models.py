# INF601 - Advanced Programming in Python
# Oumar Mballo
# Mini Project 6

"""Database models for BookNook.

Two models linked by foreign keys:
    User (one)  -> Book (many)   each book has an owner
    Genre (one) -> Book (many)   each book optionally belongs to a genre
"""

from django.conf import settings
from django.db import models


class Genre(models.Model):
    """A category a book can belong to (e.g. Fiction, Science)."""

    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Book(models.Model):
    """A single book on a user's shelf."""

    STATUS_CHOICES = [
        ("To Read", "To Read"),
        ("Reading", "Reading"),
        ("Finished", "Finished"),
    ]

    # Foreign key: each book belongs to the user who added it.
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="books",
    )
    # Foreign key: optional link to a genre.
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="books",
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="To Read"
    )
    rating = models.PositiveSmallIntegerField(
        null=True, blank=True, help_text="Optional rating from 1 to 5."
    )
    notes = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_added"]

    def __str__(self):
        return f"{self.title} by {self.author}"
