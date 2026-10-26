# INF601 - Advanced Programming in Python
# Oumar Mballo
# Mini Project 6

"""Views for the books app: public pages, auth, and book CRUD."""

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404

from .forms import BookForm
from .models import Book


def home(request):
    """Public landing page."""
    return render(request, "books/home.html")


def about(request):
    """Public about page."""
    return render(request, "books/about.html")


def register(request):
    """Let a new visitor create an account, then log them in."""
    if request.user.is_authenticated:
        return redirect("book_list")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created. Welcome to BookNook!")
            return redirect("book_list")
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {"form": form})


@login_required
def book_list(request):
    """Show the logged-in user's shelf."""
    books = Book.objects.filter(owner=request.user)
    return render(request, "books/book_list.html", {"books": books})


@login_required
def book_add(request):
    """Add a new book to the current user's shelf (form page)."""
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user  # attach the current user
            book.save()
            messages.success(request, f'"{book.title}" was added to your shelf.')
            return redirect("book_list")
    else:
        form = BookForm()

    return render(
        request, "books/book_form.html", {"form": form, "action": "Add"}
    )


@login_required
def book_edit(request, pk):
    """Edit one of the current user's books."""
    book = get_object_or_404(Book, pk=pk, owner=request.user)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, f'"{book.title}" was updated.')
            return redirect("book_list")
    else:
        form = BookForm(instance=book)

    return render(
        request, "books/book_form.html", {"form": form, "action": "Edit"}
    )


@login_required
def book_delete(request, pk):
    """Delete one of the current user's books (POST only, via modal)."""
    book = get_object_or_404(Book, pk=pk, owner=request.user)
    if request.method == "POST":
        title = book.title
        book.delete()
        messages.info(request, f'"{title}" was removed from your shelf.')
    return redirect("book_list")
