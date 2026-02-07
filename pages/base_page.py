from utils.logger import get_logger

class BasePage:

    def __init__(self, page):
        self.page = page
        self.logger = get_logger(self.__class__.__name__)

    def open(self, url):
        self.logger.info(f"Opening URL: {url}")
        self.page.goto(url)

    def is_visible(self, locator):
        return self.page.locator(locator)
