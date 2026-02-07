from pages.base_page import BasePage

class MouseActionsPOM(BasePage):

    RIGHT_CLICK_BOX = "#field1"

    def open_right_click_site(self):
        self.open("https://testautomationpractice.blogspot.com/")

    def right_click_box(self):
        self.page.locator(self.RIGHT_CLICK_BOX).click(button="right")
