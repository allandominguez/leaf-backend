# Notch

A Django-based application for managing notes.

## Project Structure

```
notch/
├── manage.py
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── apps/
    ├── auth/
    └── notes/
```

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install django
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Create a superuser:
```bash
python manage.py createsuperuser
```

5. Run the development server:
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to view the application.

## Apps

- **auth** - Authentication and user management
- **notes** - Note management functionality