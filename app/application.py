from pages.main_page import MainPage
from pages.base_page import Page


class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)

