
# Backend for accounting software

The backend is based on FastApi and SQL DB.
Currently only SQLite is implemented, should easily work with other some day.

The main.py registers the different routers.
The SQL models are in src/models, split between three categories: master data, transactions and settings.
The respective pydantic models are distributed in the same manner in the src/schemas.
The crud functions are in src/actions, split into create (update will also be there), delete and read.

Paste here the DB schema that was drawn of the table structure, cause it's some mess.
