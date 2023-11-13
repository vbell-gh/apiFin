import yaml

YAML_SETTINGS_LOCATION = "database/config.yaml"


class ApiDefault:
    """Defines the default settings for the API"""

    def __init__(self) -> None:
        self.settings = self.load_yaml()
        self.company_details = self.settings["company_details"]
        self.db_location = self.settings["data_base"]["db_location"]

        self.cash_account = self.settings["account_settings"]["cash_account"]
        self.ar_account = self.settings["account_settings"]["ar_account"]
        self.ap_account = self.settings["account_settings"]["ap_account"]
        self.vat_account = self.settings["account_settings"]["vat_account"]
        self.cogs_account = self.settings["account_settings"]["cogs_account"]

        self.log_file = self.settings["logging"]["log_file"]
        self.log_level = self.settings["logging"]["log_level"]
        self.log_format = self.settings["logging"]["log_format"]

    def load_yaml(self) -> dict:
        """load_yaml loads the yaml file with settings for the API

        Returns:
            dict: dictionary with the settings
        """
        with open(YAML_SETTINGS_LOCATION) as f:
            settings = yaml.load(f, Loader=yaml.SafeLoader)
        return settings


if __name__ == "__main__":
    settings = ApiDefault()
    print(settings.db_location)
    print(settings.cash_account)
