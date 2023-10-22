from datetime import datetime
from src.masterdata.models.gl import GLAccounts

# counrtesy of OpenAI's GPT-3
accounts_dummy = [
    # Revenue Accounts
    GLAccounts(101, "Sales Revenue", "Revenue", "Sales",
               "Goods sale", "Active", "Active", datetime.now(), 1),
    GLAccounts(102, "Sales Revenue", "Revenue", "Sales",
               "Service sales", "Active", "Active", datetime.now(), 1),
    GLAccounts(103, "Sales Discounts", "Revenue", "Sales",
               "Discounts Given", "Active", "Active", datetime.now(), 1),
    GLAccounts(104, "Rent Income", "Revenue", "Rental Income",
               "Property Rent", "Active", "Active", datetime.now(), 1),
    GLAccounts(105, "Consulting Fees", "Revenue", "Services",
               "Consulting Services", "Active", "Active", datetime.now(), 1),
    GLAccounts(106, "Cost of goods sold", "Revenue", "COGS",
               "Colst of goods sold", "Active", "Active", datetime.now(), 1),

    # Expense Accounts
    GLAccounts(201, "Secondary logistics", "Expense", "Operating",
               "Shipping Costs", "Active", "Active", datetime.now(), 1),
    GLAccounts(202, "Marketing Expense", "Expense", "Operating",
               "Marketing Costs", "Active", "Active", datetime.now(), 1),
    GLAccounts(203, "Legal Fees", "Expense", "Operating",
               "Legal Services", "Active", "Active", datetime.now(), 1),
    GLAccounts(204, "Salaries Expense", "Expense", "Operating",
               "Employee Salaries", "Active", "Active", datetime.now(), 1),

    # Asset Accounts
    GLAccounts(301, "Cash", "Asset", "Current", "Cash on Hand",
               "Active", "Active", datetime.now(), 1),
    GLAccounts(302, "Supplies", "Asset", "Current",
               "Office Supplies", "Active", "Active", datetime.now(), 1),
    GLAccounts(303, "Inventory", "Asset", "Current",
               "Stocked Items", "Active", "Active", datetime.now(), 1),
    GLAccounts(304, "Accounts Receivable", "Asset", "Current",
               "Unpaid Invoices", "Active", "Active", datetime.now(), 1),
    GLAccounts(305, "Equipment", "Asset", "Fixed",
               "Office Equipment", "Active", "Active", datetime.now(), 1),
    GLAccounts(306, "Office Furniture", "Asset", "Fixed",
               "Office Furniture", "Active", "Active", datetime.now(), 1),
    GLAccounts(307, "Prepaid Expenses", "Asset", "Current",
               "Advance Payments", "Active", "Active", datetime.now(), 1),

    # Liability Accounts
    GLAccounts(401, "Accounts Payable", "Liability", "Current",
               "Unpaid Bills", "Active", "Active", datetime.now(), 1),

    # Equity Accounts
    GLAccounts(501, "Owner's Equity", "Equity", None,
               None, "Active", "Active", datetime.now(), 1)
]
