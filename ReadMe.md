
**Backend for accounting software**

The backend is based on FastApi and SQL DB.
Currently only SQLite is implemented, who knows some day maybe something else.

The main.py registers the different routers.
The masterdata is in src/masterdata/ where each has crud and model files the following models:
    Users and roles: add, remove, list users. Each users can be assigned a role, based on which actions can be defined.
    Counter parties: add, remove, list counterparties. Each counterparty has items, including: Name, type, due-days, contacts, etc.
    GL: defines the general ledger of the comapny, each account has atributes, this needs to be developed further
