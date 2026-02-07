from playwright.sync_api import Page
from pages.base_page import BasePage


class TablePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.table = self.page.locator("table[name='BookTable']")

    # ---------- BASIC ACTIONS ----------

    def open_page(self):
        self.page.goto("https://testautomationpractice.blogspot.com/")

    def is_table_visible(self):
        return self.table

    # ---------- ROW & COLUMN ----------

    def get_rows(self):
        return self.table.locator("tr")

    def get_row_count(self):
        return self.get_rows().count()

    def get_column_count(self):
        return self.table.locator("th").count()

    # ---------- READ DATA ----------

    def get_second_row_data(self):
        row = self.get_rows().nth(1).locator("td")
        return row.all_inner_texts()

    def get_all_rows_data(self):
        all_rows = self.get_rows().all()
        table_data = []
        for row in all_rows[1:]:  # skip header
            table_data.append(row.locator("td").all_inner_texts())
        return table_data

    # ---------- FILTER DATA ----------

    def get_books_by_author(self, author_name):
        books = []
        all_rows = self.get_rows().all()

        for row in all_rows[1:]:
            author = row.locator("td").nth(1).inner_text()
            if author == author_name:
                book = row.locator("td").nth(0).inner_text()
                books.append(book)

        return books

    # ---------- AGGREGATION ----------

    def get_total_price(self):
        total_price = 0
        all_rows = self.get_rows().all()

        for row in all_rows[1:]:
            price = int(row.locator("td").nth(3).inner_text())
            total_price += price

        return total_price
