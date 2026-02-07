import pytest
from playwright.sync_api import expect


def test_select_country_by_label(dropdown_pom):
    """
    WHAT TO TEST:
    - Open the page
    - Verify dropdown is visible & enabled
    - Select country using label
    - Validate selected value
    """

    dropdown_pom.open("https://testautomationpractice.blogspot.com/")

    dropdown = dropdown_pom.get_country_dropdown()

    expect(dropdown).to_be_visible()
    expect(dropdown).to_be_enabled()

    dropdown_pom.select_country_by_label("India")
    expect(dropdown).to_have_value("india")


def test_select_country_by_value(dropdown_pom):
    """
    WHAT TO TEST:
    - Select country using value
    - Validate selected value
    """

    dropdown_pom.open("https://testautomationpractice.blogspot.com/")
    dropdown_pom.select_country_by_value("uk")

    dropdown = dropdown_pom.get_country_dropdown()
    expect(dropdown).to_have_value("uk")


def test_country_dropdown_options_count(dropdown_pom):
    """
    WHAT TO TEST:
    - Validate number of dropdown options
    """

    dropdown_pom.open("https://testautomationpractice.blogspot.com/")

    options = dropdown_pom.get_all_country_options()
    count = dropdown_pom.get_dropdown_count()
    assert count == 10

