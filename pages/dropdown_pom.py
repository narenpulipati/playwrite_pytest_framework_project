# pages/dropdown_pom.py

from pages.base_page import BasePage


class DropdownPOM(BasePage):

    COUNTRY_DROPDOWN = "#country"

    def select_country_by_label(self, label):
        self.page.select_option(self.COUNTRY_DROPDOWN, label=label)

    def select_country_by_value(self, value):
        self.page.select_option(self.COUNTRY_DROPDOWN, value=value)

    def get_selected_value(self):
        return self.page.locator(self.COUNTRY_DROPDOWN).input_value()

    def get_options_count(self):
        return self.page.locator(f"{self.COUNTRY_DROPDOWN} option").count()
