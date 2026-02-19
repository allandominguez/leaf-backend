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

## Apps

- **users** - Authentication and user management
- **notes** - Note management functionality

## Development

### Prerequisites
- Python 3.11+
- pip-tools (`pip install pip-tools`)
- PostgreSQL (for production, SQLite for local dev)

### Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip-sync requirements-dev.txt
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

### Branch naming scheme
For new feature branches, use:
```
add/*
update/*
```

For bugfix branches, use:
```
fix/*
```

For maintenance branches, use:
```
improve/*
chore/*
```

### Managing dependencies

We use `pip-tools` to manage dependencies for reproducible builds.

#### Adding a New Dependency

**For production dependencies:**

1. Add package to `requirements.in`:
```bash
echo "package-name" >> requirements.in
```

2. Compile and sync:
```bash
pip-compile requirements.in         # compiles prod requirements
pip-compile requirements-dev.in     # compiles dev requirements (which includes prod)
pip-sync requirements-dev.txt       # this installs all requirements locally
```

3. Commit both `.in` and `.txt` files:
```bash
git add requirements.in requirements.txt
git commit -m "Add package-name dependency"
```

**For development-only dependencies (testing, linting, etc):**

1. Add to `requirements-dev.in`:
```bash
echo "pytest-mock" >> requirements-dev.in
```

2. Compile and sync:
```bash
pip-compile requirements-dev.in
pip-sync requirements-dev.txt
```

3. Commit:
```bash
git add requirements-dev.in requirements-dev.txt
git commit -m "Add pytest-mock for testing"
```

### Updating Dependencies

**Update a specific package:**
```bash
pip-compile --upgrade-package django requirements.in
pip-sync requirements-dev.txt
```

**Update all packages:**
```bash
pip-compile --upgrade requirements.in
pip-compile --upgrade requirements-dev.in
pip-sync requirements-dev.txt
```

**Always test after updating:**
```bash
pytest
python manage.py check
```
