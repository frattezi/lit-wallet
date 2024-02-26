# Lit Wallet

This is a simple API + Streamlit APP written in python.

## Technologies

- Python
- FastAPI
- Streamlit
- Docker
- Docker Compose
- Poetry
- Pytest
- Black

## How to run

### Docker

Currently, we only run the database for this project in a docker compose. Our plan is to also add services and run everything with docker.

```bash
docker-compose up
```

So, before running the project. Remember to install docker and docker-compose. And run the above command so the database is open for connections from the App.

### API and streamlit app

```bash
# Make sure you have poe installed
pipx install poethepoet

# Make sure you install the dependencies in the first run
poetry install

# Now you can run commands with poe, find other commands in the pyproject.toml file

# Starts up the api
poe api

# Starts up the app
poe app

# Linting
poe lint

# Run tests -TBD
poe test
```
