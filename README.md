# Leaf

A fast, minimal, page‑based thinking tool — not a traditional notes manager.

_Open → write instantly → close → move on._ 

## Project Structure

```
leaf/
├── manage.py
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── apps/
    ├── users/
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
pip install -r requirements.txt
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

## Contributing
For new feature branches use:
```
add/*
update/*
```

For bugfix branches use:
```
fix/*
```

For maintenance branches use:
```
improve/*
chore/*
```

## Apps

- **users** - Authentication and user management
- **notes** - Note management functionality