# pages/mouse_actions_pom.py

from pages.base_page import BasePage


class MouseActionsPOM(BasePage):

    RIGHT_CLICK_BOX = "#hot-spot"

    def right_click(self):
        self.page.locator(self.RIGHT_CLICK_BOX).click(button="right")
