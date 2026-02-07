from pages.css_page import CssPage
from playwright.sync_api import expect


def test_css_selectors(page):
    css_page = CssPage(page)

    css_page.open_page()

    css_page.fill_user_details(
        name="Narendra Pulipati",
        email="pulipati@123.com",
        address="Hyderabad"
    )

    css_page.select_gender("")
    css_page.select_days()

    all_days = css_page.get_all_days()
    print("Available days:", all_days)

    css_page.click_day_by_index(5)
    css_page.click_day_by_index(3)

    expect(page).to_have_title("Automation Testing Practice")
