from pages.base_page import BasePage

class DropdownPOM(BasePage):

    COUNTRY = "#country"

    def get_country_dropdown(self):
        return self.page.locator(self.COUNTRY)

    def get_all_country_options(self):
        return self.page.locator(f"{self.COUNTRY} option").all_text_contents()

    def select_country_by_label(self, label):
        self.page.select_option(self.COUNTRY, label=label)

    def select_country_by_value(self, value):
        self.page.select_option(self.COUNTRY, value=value)

    def get_dropdown_count(self):
        return self.page.locator(f"{self.COUNTRY} option").count()
