from pages.base_page import BasePage

class CssPage(BasePage):

    NAME = "#name"
    EMAIL = "#email"
    ADDRESS = "#textarea"

    GENDER_MALE = "#male"
    GENDER_FEMALE = "#female"

    DAYS = "input[type='checkbox']"

    def fill_user_details(self, name, email, address):
        self.page.fill(self.NAME, name)
        self.page.fill(self.EMAIL, email)
        self.page.fill(self.ADDRESS, address)

    def select_gender(self, gender):
        if gender.lower() == "male":
            self.page.check(self.GENDER_MALE)
        elif gender.lower() == "female":
            self.page.check(self.GENDER_FEMALE)

    def select_days(self):
        pass   # test calls it — keep placeholder

    def get_all_days(self):
        return self.page.locator(self.DAYS).all()

    def click_day_by_index(self, index):
        self.page.locator(self.DAYS).nth(index).check()
