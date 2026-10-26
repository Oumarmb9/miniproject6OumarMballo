# INF601 - Advanced Programming in Python
# Oumar Mballo
# Mini Project 6

"""Forms for the books app."""

from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    """Add / edit form for a Book.

    The owner is set automatically in the view, so it is not shown here.
    """

    class Meta:
        model = Book
        fields = ["title", "author", "genre", "status", "rating", "notes"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "genre": forms.Select(attrs={"class": "form-select"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "rating": forms.NumberInput(
                attrs={"class": "form-control", "min": 1, "max": 5}
            ),
            "notes": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

    def clean_rating(self):
        """Keep the rating within 1-5 when one is given."""
        rating = self.cleaned_data.get("rating")
        if rating is not None and not (1 <= rating <= 5):
            raise forms.ValidationError("Rating must be between 1 and 5.")
        return rating
