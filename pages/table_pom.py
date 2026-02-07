# pages/table_pom.py

from pages.base_page import BasePage


class TablePOM(BasePage):

    TABLE = "table[name='BookTable']"
    ROWS = "tr"
    COLUMNS = "th"

    def verify_table_visible(self):
        return self.is_visible(self.TABLE)

    def get_row_count(self):
        return self.page.locator(f"{self.TABLE} {self.ROWS}").count()

    def get_column_count(self):
        return self.page.locator(f"{self.TABLE} {self.COLUMNS}").count()
