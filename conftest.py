import os
import pytest
from playwright.sync_api import sync_playwright
from pages.mouse_actions_pom import MouseActionsPOM


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page


# 🔹 POM fixture (THIS WAS MISSING)
@pytest.fixture
def mouse_actions_pom(page):
    return MouseActionsPOM(page)


# 🔹 Screenshot on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs("screenshots", exist_ok=True)
            page.screenshot(path=f"screenshots/{item.name}.png")
import pytest
from pages.mouse_actions_pom import MouseActionsPOM


@pytest.fixture
def mouse_actions_pom(page):
    return MouseActionsPOM(page)
from pages.table_pom import TablePOM

@pytest.fixture
def table_pom(page):
    return TablePOM(page)

from pages.form_pom import FormPOM

@pytest.fixture
def form_pom(page):
    return FormPOM(page)


from pages.dropdown_pom import DropdownPOM

@pytest.fixture
def dropdown_pom(page):
    return DropdownPOM(page)


import os
import pytest
import allure

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs("reports/screenshots", exist_ok=True)
            screenshot_path = f"reports/screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)

            # Attach to Allure
            allure.attach.file(
                screenshot_path,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
