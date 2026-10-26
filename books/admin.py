# INF601 - Advanced Programming in Python
# Oumar Mballo
# Mini Project 6

"""Django admin configuration, styled for easy data entry."""

from django.contrib import admin

from .models import Book, Genre


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Columns shown in the book list page of the admin.
    list_display = ("title", "author", "owner", "genre", "status", "rating", "date_added")
    # Right-hand filters for quickly narrowing the list.
    list_filter = ("status", "genre", "date_added")
    # Search box fields.
    search_fields = ("title", "author", "owner__username")
    # Let the user set the owner/genre with a dropdown and order newest first.
    autocomplete_fields = ("genre",)
    date_hierarchy = "date_added"
    # Group the fields nicely on the add/edit form.
    fieldsets = (
        ("Book", {"fields": ("title", "author", "genre")}),
        ("Reading progress", {"fields": ("status", "rating", "notes")}),
        ("Ownership", {"fields": ("owner",)}),
    )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
