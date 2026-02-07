from pages.base_page import BasePage

class TablePOM(BasePage):

    TABLE = "table[name='BookTable']"

    def get_row_count(self):
        return self.page.locator(f"{self.TABLE} tr").count()

    def get_column_count(self):
        return self.page.locator(f"{self.TABLE} th").count()

    def get_row_data(self, index):
        rows = self.page.locator(f"{self.TABLE} tr")
        data_row = rows.nth(index)  # remove +1
        cells = data_row.locator("td")
        return [cells.nth(i).inner_text() for i in range(cells.count())]

    def get_all_rows_data(self):
        rows = self.page.locator(f"{self.TABLE} tr").all()
        data = []
        for r in rows[1:]:
            data.append(r.locator("td").all_text_contents())
        return data

    def get_books_by_author(self, author):
        rows = self.get_all_rows_data()
        return [r[0] for r in rows if r[1] == author]

    def get_total_price(self):
        rows = self.get_all_rows_data()
        return sum(int(r[3]) for r in rows)



