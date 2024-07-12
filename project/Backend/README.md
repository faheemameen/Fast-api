##### Install Packages

```
poetry add fastapi,sqlmodel
poetry add uvicorn(for server)
poetry add "psycopg[standard]"
```

##### for testing install packages

```
poetry add pytest
poetry add httpx
```

##### for running server

`poetry run uvicorn app.main:app --reload`

##### for checking test

```
poetry run pytest
poetry run pytest -vv (for checking details)
```
