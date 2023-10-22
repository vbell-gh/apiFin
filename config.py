class ApiDefault:
    def __init__(self) -> None:
        self.development = True
        self.database_is_sqllite = True
        self.database_location = "database"
        self.company_name = "CompanyX"
        self.currency = "BGN"
        self.company_details = self.compnay_details()

    def compnay_details(self):
        details = {
            "company_name": self.company_name,
            "currency": self.currency,
            "company_address": "Sofia, Bulgaria",
            "company_phone": "+359 888 888 888",
            "company_email": "ceo@companyx.bg",
            "VATID": "BG123456789",
            "ID": "123456789",
        }
        return details
