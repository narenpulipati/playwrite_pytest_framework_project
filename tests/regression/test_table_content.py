from pages.table_page import TablePage
from playwright.sync_api import expect


def test_table_static(page):
    table_page = TablePage(page)

    table_page.open_page()

    # table visible
    expect(table_page.is_table_visible()).to_be_visible()

    # rows & columns
    rows = table_page.get_row_count()
    cols = table_page.get_column_count()
    print("Rows:", rows)
    print("Columns:", cols)

    # second row validation
    second_row = table_page.get_second_row_data()
    print("Second row:", second_row)
    assert second_row == ['Learn Selenium', 'Amit', 'Selenium', '300']

    # print all data
    all_data = table_page.get_all_rows_data()
    for row in all_data:
        print(row)

    # books by Amit
    books = table_page.get_books_by_author("Amit")
    print("Books by Amit:", books)

    # total price
    total_price = table_page.get_total_price()
    print("Total price:", total_price)
