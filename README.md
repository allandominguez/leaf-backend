[![Test workflow](https://github.com/allandominguez/leaf-backend/actions/workflows/test.yml/badge.svg)](https://github.com/allandominguez/leaf-backend/actions/workflows/test.yml)
[![Lint workflow](https://github.com/allandominguez/leaf-backend/actions/workflows/lint.yml/badge.svg)](https://github.com/allandominguez/leaf-backend/actions/workflows/lint.yml)

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

### Code Quality
This project uses [ruff](https://docs.astral.sh/ruff/) for linting and formatting.

Run the linter:
```bash
ruff check .
```

Run the linter with auto-fix:
```bash
ruff check --fix .
```

Run the formatter:
```bash
ruff format .
```

#### Pre-commit configuration
Pre-commit hooks has also been configured to run `ruff` and [detect-secrets](https://github.com/Yelp/detect-secrets). To install them:
```bash
pre-commit install
```

### Tests
Run the test suite:
`pytest --tb=short`

With coverage:
`pytest --tb=short --cov=. --cov-report=term-missing`


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
pip-compile requirements.in         # compiles prod requirements (requirements.txt)
pip-compile requirements-dev.in     # compiles dev requirements, including prod (requirements-dev.txt)
pip-sync requirements-dev.txt       # this installs all requirements locally (requirements-dev.txt)
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
