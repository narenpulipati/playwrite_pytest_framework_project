from playwright.sync_api import Page
from pages.base_page import BasePage


class FormPOM(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def open_form_page(self):
        self.page.goto("https://testautomationpractice.blogspot.com/")

    def fill_name(self, name):
        self.page.locator("#name").fill(name)

    def fill_email(self, email):
        self.page.locator("#email").fill(email)

    def fill_address(self, address):
        self.page.locator("#textarea").fill(address)

    def submit_form(self):
        self.page.locator("input[type='submit']").click()
