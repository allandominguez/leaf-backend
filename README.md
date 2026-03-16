[![Build](https://github.com/allandominguez/leaf-backend/actions/workflows/build.yml/badge.svg)](https://github.com/allandominguez/leaf-backend/actions/workflows/build.yml)
[![Test workflow](https://github.com/allandominguez/leaf-backend/actions/workflows/test.yml/badge.svg)](https://github.com/allandominguez/leaf-backend/actions/workflows/test.yml)
[![Lint workflow](https://github.com/allandominguez/leaf-backend/actions/workflows/lint.yml/badge.svg)](https://github.com/allandominguez/leaf-backend/actions/workflows/lint.yml)

# Leaf

> **Status:** 🚧 Early-stage prototype. Core user models and authentication being implemented.

A fast, minimal, page‑based thinking tool — not a traditional notes manager.

**_Open → write instantly → close → move on._**

## Key Features (Planned)

- **Instant capture** - Opens to blank page in <1 second
- **Page limits** - Fixed capacity per note (like physical pages)
- **Finite memory** - Notebook holds 64-192 pages, oldest expire automatically
- **Simple filing** - Two-level directory system for important notes
- **Single pin** - One pinned note (grocery list, packing list, etc.)
- **Photo support** - One photo per note as visual anchor
- **Offline-first** - Works without internet, syncs when available

## Tech Stack

**Backend:**
- Django 6.0 + Django REST Framework (planned)
- PostgreSQL (production) / SQLite (development)
- Django REST Knox (token authentication - planned)
- Supabase Storage (photos - planned)

**Mobile:** (planned)
- React Native (Expo)
- TypeScript
- React Navigation

**DevOps:**
- pytest + pytest-django (testing)
- ruff (linting and formatting)
- uv (dependency management)
- GitHub Actions (CI/CD)
- pre-commit hooks
- Railway/Render (deployment - planned)

## Roadmap

See [Initiative & Epic Plan](docs/initiative-plan.md) for detailed breakdown.

**Phase 1 (Current):** Foundation & Authentication  
**Phase 2:** Core Note Features  
**Phase 3:** Mobile UI & Navigation  
**Phase 4:** Polish & Deployment  
**Phase 5:** Post-Launch Iteration

## Project Structure
```
leaf/
├── manage.py
├── pyproject.toml
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
- Python 3.13+
- [uv](https://docs.astral.sh/uv/)

### Setup
1. Install uv:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Install dependencies:
```bash
uv sync --dev
```

3. Install pre-commit hooks:
```bash
uv run pre-commit install
```

4. Run migrations:
```bash
uv run python manage.py migrate
```

5. Create a superuser:
```bash
uv run python manage.py createsuperuser
```

6. Run the development server:
```bash
uv run python manage.py runserver
```

Visit `http://127.0.0.1:8000` to view the application.

### Managing Dependencies

Dependencies are managed via `pyproject.toml` and `uv`.

#### Adding a dependency
```bash
uv add django-filter          # production
uv add --dev pytest-mock      # development only
```

#### Updating dependencies
```bash
uv sync --dev
```

Always test after updating:
```bash
uv run pytest
uv run python manage.py check
```

### Code Quality

This project uses [ruff](https://docs.astral.sh/ruff/) for linting and formatting.

Run the linter:
```bash
uv run ruff check .
```

Run the linter with auto-fix:
```bash
uv run ruff check --fix .
```

Run the formatter:
```bash
uv run ruff format .
```

Pre-commit hooks are configured to run both automatically on each commit. To install them:
```bash
uv run pre-commit install
```

### Tests

Run the test suite:
```bash
uv run pytest --tb=short
```

With coverage:
```bash
uv run pytest --tb=short --cov=. --cov-report=term-missing
```

## Branching

| Branch | Purpose |
|--------|---------|
| `main` | Production-ready code |
| `add/desc`, `update/desc` | New features |
| `fix/desc` | Bug fixes |
| `chore/desc`, `improve/desc` | Maintenance tasks (dependencies, config etc.) |

## Project Goals 

The core of this project was just being able to **continue my joy of building and maintaining software**.

Additionally, I want to use it as a way to explore and expand my skillset as a product-focused software engineer. So I also hope to demonstrate:

**Product focused thinking:**
- Translating a product vision into technical implementation
- Building with constraints to improve user experience

**Technical Skills:**
- Modern REST API design with Django
- Mobile app development with React Native (planned)
- Authentication and authorization patterns
- Offline-first architecture with sync (planned)
- Test-driven development practices
- CI/CD pipeline setup
- Production deployment and monitoring (planned)

**Professional Practices:**
- Clean git history and meaningful commits
- Comprehensive testing and test coverage (unit, integration, API)
- Exploring dependency management with **uv** 
- Code quality automation (linting, formatting, pre-commit hooks)
- Documentation and code organization

## Contributing

This is primarily a personal portfolio project, but feedback and suggestions are welcome! Feel free to:
- Open issues for bugs or suggestions
- Share thoughts on the constraint-based approach
- Suggest improvements to architecture or code quality

**Note:** As this is a learning project, I'm intentionally building features myself rather than accepting PRs, but discussion is encouraged.

## License

MIT License - see [LICENSE](.github/LICENSE) file for details

## Contact

**Allan Dominguez**  
[Portfolio](https://allandominguez.dev/) | [GitHub](https://github.com/allandominguez) | [LinkedIn](https://www.linkedin.com/in/allan-dominguez-113625146/) | [Email](mailto:allan.c.dominguez@gmail.com)

*This project is part of my portfolio demonstrating full-stack product development capabilities.*