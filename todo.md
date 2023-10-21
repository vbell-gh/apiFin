Master data:
    Done:
        GL - Trial balance - includes attributes of each account - this needs to be developed further with time
        Counter parties - includes main + atributes with 3 docs attached each and contacts
        Users - includes users + roles passwords need to be crypted, now strings are stored
    Not done:
        Cost/profit centers
        Invenotry
        Bank accounts
        Warehouses

Transactions:
    Not done:
        Document tables, that add data to GL tables, however the document tables are more detailed
        GL Tables
        Invoice issuing:
            Issuing invoices for services - the underlying transaction to be recorded in services view, simple DR AR / CR REV
            Issuing invoices for goods - posting need to incude DR AR / CR REV, COST OF SALE / CR INVENOTRY (FIFO/AVG)
        Invoice reciving:
            Invoices for service/goods - directly expensed DR Expense / CR AP - invoice recognition and selection
            Invoices accumulated in invenotry 
        Bank postings, close invoice tracking in addition posts transcatio to GL table
        

Views:
    Not done
