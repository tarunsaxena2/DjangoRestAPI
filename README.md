# Django REST API - User Management

This project provides User CRUD APIs using Django and Django REST Framework.

## Features

- Create user
- List users
- Retrieve user
- Update user
- Delete user
- Session authentication
- Token authentication
- User permissions
- Search
- Filtering
- Ordering
- Pagination

## API Endpoints

- GET /api/users/
- POST /api/users/
- GET /api/users/<id>/
- PUT /api/users/<id>/
- PATCH /api/users/<id>/
- DELETE /api/users/<id>/

## Installation

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


README ko bahut professional ya unnecessarily long mat banana. Simple rakho aur jo samjha hai wahi likho.

---

# Part 21 — Final project structure

Final structure:

```text
DjangoRestAPI-Tarun/
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── users/
│   ├── migrations/
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── db.sqlite3
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore