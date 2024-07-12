# FastAPI:

- FastAPI is a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints.
  [Documentation](https://fastapi.tiangolo.com/)

# Poetry

- Poetry is a tool for dependency management and packaging in Python. By default, Poetry creates a virtual environment.
  [Documentation](https://python-poetry.org/docs/)

---

- Create new Python project with poetry

`poetry new hello-world`

- This will create the hello-world directory with the following content:

>     hello-world
>     ├── pyproject.toml
>     ├── README.md
>     ├── hello-world
>         └── __init__.py
>     └── tests
>          └── __init__.py

- If you want to name your project differently than the folder, you can pass the --name option:

`poetry new  hello-world --name app`

>      hello-world
>      ├── pyproject.toml
>      ├── README.md
>      ├── app
>          └── __init__.py
>      └── tests
>          └── __init__.py

- The pyproject.toml file is what is the most important here. This will orchestrate your project and its dependencies.
>      [tool.poetry]
>      name = "hello-world"
>      version = "0.1.0"
>      description = ""
>      authors = ["faheemameen <mohammadfaheem514@gmail.com>"]
>      readme = "README.md"
>
>     [tool.poetry.dependencies]
>      python = "^3.12"
>     pytest = "^8.1.1"
>      fastapi = "^0.110.1"
>     uvicorn = {extras = ["standard"], version = "^0.29.0"}
>
>     [build-system]
>     requires = ["poetry-core"]
>     build-backend = "poetry.core.masonry.api"




- This command adds required packages to your pyproject.toml and installs them:

`poetry add fastapi`

- The remove command removes a package from the current list of installed packages:

`poetry remove fastapi`

- To list all the available packages, you can use the show command:

`poetry show`

- This command starts a new shell and activates the virtual environment:

`poetry shell`
