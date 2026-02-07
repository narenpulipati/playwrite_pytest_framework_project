def test_table_data(table_pom):
    table_pom.open("https://testautomationpractice.blogspot.com/")

    assert table_pom.get_row_count() > 1
    assert table_pom.get_column_count() == 4

    second_row = table_pom.get_row_data(1)
    assert second_row == ['Learn Selenium', 'Amit', 'Selenium', '300']

    books = table_pom.get_books_by_author("Amit")
    assert "Learn Selenium" in books

    total_price = table_pom.get_total_price()
    assert total_price > 0
