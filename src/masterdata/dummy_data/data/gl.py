from datetime import datetime
from src.masterdata.models.gl import GLAccounts

# counrtesy of OpenAI's GPT-3
accounts_dummy = [
    # Revenue Accounts
    GLAccounts(account_code=101, account_name="Sales Revenue", account_type="Revenue",
               account_category="Sales", account_subcategory="Product Sales",
               account_description="Active", account_status="Active", account_created=datetime.now(), account_creator=1),
    GLAccounts(account_code=102, account_name="Interest Income", account_type="Revenue",
               account_category="Interest", account_subcategory="Earned Interest",
               account_description="Active", account_status="Active", account_created=datetime.now(), account_creator=1),
    GLAccounts(account_code=103, account_name="Sales Discounts", account_type="Revenue",
               account_category="Sales", account_subcategory="Discounts Given",
               account_description="Active", account_status="Active", account_created=datetime.now(), account_creator=1),
    GLAccounts(account_code=104, account_name="Rent Income", account_type="Revenue",
               account_category="Rental Income", account_subcategory="Property Rent",
               account_description="Active", account_status="Active", account_created=datetime.now(), account_creator=1),
    GLAccounts(account_code=105, account_name="Consulting Fees", account_type="Revenue",
               account_category="Services", account_subcategory="Consulting Services",
               account_description="Active", account_status="Active", account_created=datetime.now(), account_creator=1),

    # Expense Accounts
    GLAccounts(account_code=201, account_name="Shipping Expenses", account_type="Expense",
               account_category="Operating", account_subcategory="Shipping Costs",
               account_description="Active", account_status="Active", account_created=datetime.now(), account_creator=1),
    GLAccounts(account_code=202, account_name="Marketing Expense", account_type="Expense",
               account_category="Operating", account_subcategory="Marketing Costs",
               account_description="Active", account_status="Active", account_created=datetime.now(), account_creator=1),
    GLAccounts(account_code=203, account_name="Legal Fees", account_type="Expense",
               account_category="Operating", account_subcategory="Legal Services",
               account_description="Active", account_status="Active", account_created=datetime.now(), account_creator=1),
    GLAccounts(account_code=204, account_name="Salaries Expense", account_type="Expense",
               account_category="Operating", account_subcategory="Employee Salaries",
               account_description="Active", account_status="Active", account_created=datetime.now(), account_creator=1),

    # Asset Accounts
    GLAccounts(account_code=301, account_name="Cash", account_type="Asset",
               account_category="Current", account_subcategory="Cash on Hand",
               account_description="Active", account_status="Active", account_created=datetime.now(), account_creator=1),
    GLAccounts(account_code=302, account_name="Supplies", account_type="Asset",
               account_category="Current", account_subcategory="Office Supplies",
               account_description="Active", account_status="Active", account_created=datetime.now(), account_creator=1),
    GLAccounts(account_code=303, account_name="Inventory", account_type="Asset",
               account_category="Current", account_subcategory="Stocked Items",
               account_description="Active", account_status="Active", account_created=datetime.now(), account_creator=1),
    GLAccounts(account_code=304, account_name="Accounts Receivable", account_type="Asset",
               account_category="Current", account_subcategory="Unpaid Invoices",
               account_description="Active", account_status="Active", account_created=datetime.now(), account_creator=1),
    GLAccounts(account_code=305, account_name="Equipment", account_type="Asset",
               account_category="Fixed", account_subcategory="Office Equipment",
               account_description="Active", account_status="Active", account_created=datetime.now(), account_creator=1),
    GLAccounts(account_code=306, account_name="Office Furniture", account_type="Asset",
               account_category="Fixed", account_subcategory="Office Furniture",
               account_description="Active", account_status="Active", account_created=datetime.now(), account_creator=1),
    GLAccounts(account_code=307, account_name="Prepaid Expenses", account_type="Asset",
               account_category="Current", account_subcategory="Advance Payments",
               account_description="Active", account_status="Active", account_created=datetime.now(), account_creator=1),

    # Liability Accounts
    GLAccounts(account_code=401, account_name="Accounts Payable", account_type="Liability",
               account_category="Current", account_subcategory="Unpaid Bills",
               account_description="Active", account_status="Active", account_created=datetime.now(), account_creator=1),

    # Equity Accounts
    GLAccounts(account_code=501, account_name="Owner's Equity", account_type="Equity",
               account_category=None, account_subcategory=None,
               account_description="Active", account_status="Active", account_created=datetime.now(), account_creator=1)
]
