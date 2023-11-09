SQL and pydantic models:
    Done:
        GL: MD and transactions
        Vendords/ Clients: MD and transactions
        Invenotry MD and respective transactions <- fifo, lifo AVG
        Users <- needs to be improved, also hash pass
        Sales MD and transactions
    Not done:
        
        Bank accounts <- mapping
        Warehouses <- not mandatory but would be nice, not turning this into WMS
        Paste DB schema after testint, cause most probably there will be changes again
        Learn how to do proper documentation
        Check if docstrings are really a must everywhere, cause it seems pointless
    Think:
        Cost/profit centers <- either some sort of subcategories or full implementation in in GL transactions, not sure should decide some day.
        Transaction flow for documents, one posting or multiple document based.
        Azure Document AI implementation test confidence levels first.

    Later:
        Auto account selection based on history + rows
        Bank posting based on vendor account and SWIFT text
        Payroll <- Not sure if this should be implemented at all

TRY POSTMAN for testing the API
