# BookNook — INF601 Mini Project 6

**Oumar Mballo · INF601 – Advanced Programming in Python**

BookNook is a small Django web application for keeping track of the books you read.
Each user registers an account, logs in, and manages a private bookshelf: add a book
with its genre, reading status, an optional 1–5 star rating, and notes, edit it later,
and remove it with a confirmation dialog. A styled Django admin lets a superuser manage
all books and genres.

## Features

- Seven pages built on a shared Jinja/Django template (Home, About, Register, Log In,
  My Shelf, Add Book, Edit Book).
- Register / log in / log out using Django's built-in authentication system.
- A **SQLite database with two models linked by a foreign key** — `Book → User` (owner)
  and `Book → Genre`.
- **Add** and **Edit** pages driven by a Django `ModelForm`.
- A **styled Django admin** (`list_display`, `list_filter`, `search_fields`, grouped
  fieldsets) for easy data entry.
- **Bootstrap 5** styling, including a **modal** that confirms before a book is deleted.
- Each user only ever sees and edits their own books.

## Project structure

```
miniproject6OumarMballo/
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── booknook/              # project package (settings, URLs, WSGI/ASGI)
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── books/                 # the app
    ├── __init__.py
    ├── admin.py           # styled admin
    ├── apps.py
    ├── forms.py           # BookForm (ModelForm)
    ├── models.py          # Book + Genre (foreign keys)
    ├── urls.py
    ├── views.py           # public pages, auth, book CRUD
    ├── tests.py
    ├── migrations/
    │   └── __init__.py
    └── templates/
        ├── base.html
        ├── books/
        │   ├── home.html
        │   ├── about.html
        │   ├── book_list.html   # shelf + delete modal
        │   └── book_form.html   # add / edit form
        └── registration/
            ├── login.html
            └── register.html
```

The SQLite database (`db.sqlite3`) is created at runtime and is git-ignored.

## Setup and running

You need Python 3.10+.

**1. (Optional) create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

**2. Install the requirements**

```bash
pip install -r requirements.txt
```

**3. Initialize the database**

```bash
python manage.py makemigrations
python manage.py migrate
```

**4. Create an admin (superuser) account**

```bash
python manage.py createsuperuser
```

**5. Run the development server**

```bash
python manage.py runserver
```

Then open <http://127.0.0.1:8000> for the app, or <http://127.0.0.1:8000/admin> for the
Django admin (log in with the superuser you created).

## How to use it

1. Click **Register** and create an account (or log in).
2. Go to **Add Book**, fill in the form, and submit — the book appears on **My Shelf**.
3. Click **Edit** to change any of a book's details.
4. Click **Delete** to open the confirmation modal and remove a book.
5. Visit **/admin** as a superuser to manage all books and genres.

> Tip: add a few `Genre` rows in the admin first (e.g. Fiction, Science, History) so they
> appear in the book form's genre dropdown.

## AI Usage

I used an AI assistant (Claude) as a helper while building this project, in line with the
course AI Use Policy. AI was used to scaffold the Django project and app layout, draft the
models, views, forms, admin configuration, and the Bootstrap templates, and to help write
this README.

What I changed in the AI-generated code after it was produced:

- Set the `owner` foreign key to `settings.AUTH_USER_MODEL` and made `book_add`/`book_edit`
  attach `request.user` and filter the shelf so each user only sees their own books.
- Restricted `book_edit`/`book_delete` with `get_object_or_404(Book, pk=pk, owner=request.user)`
  so a user cannot reach another user's book by changing the URL.
- Switched the logout link to a POST form, since Django 5 no longer allows logout via GET.
- Added the `clean_rating` validation on `BookForm` to keep ratings between 1 and 5.
- Styled the admin (`list_display`, `list_filter`, `search_fields`, grouped `fieldsets`) and
  tuned the templates (status badges, the notes row, and the delete-confirmation modal).

I reviewed and tested all of the code myself and confirmed the app meets the project
requirements before submitting. All final decisions and the submitted work are my own.
