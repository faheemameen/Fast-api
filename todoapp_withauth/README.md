## FastAPI with Authentication

### Packages that used in this project:

`poetry add "psycopg[binary]"`

- Psycopg is a PostgreSQL adapter for the Python programming language

`poetry add python-multipart`

- Python-Multipart is a library for handling multipart/form-data POST requests. This is usually only needed or used when running a web server and you have a place where users can upload files.

`poetry add "passlib[bcrypt]" `

- PassLib is a great Python package to handle password hashes

`poetry add "python-jose[crytography]`

- specifically indicates that you're installing the python-jose library along with the cryptography backend. This backend provides secure cryptographic operations that are essential for the security aspects of JWTs(JSON Web Tokens), JWEs( JSON Web Encryption), JWKs(JSON Web Keys), etc.

`openssl rand --hex 32`

- used for generate random string

#### To run the project run this command:

`poetry run uvicorn main.app:app --reload`


