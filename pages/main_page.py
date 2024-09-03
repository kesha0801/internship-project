from selenium.webdriver.common.by import By
#from pages.header import Header
from pages.base_page import Page
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


class MainPage(Page):
    OFF_PLAN_BTN = (By.XPATH, "//div[@class='menu-button-text' and text()='Off-plan']")
    OFF_PLAN_OPENS = (By.XPATH, "//div[@class='page-title off_plan']")
    SALES_STATUS_BTN = (By.XPATH, "//select[@id='Location-2']")
    ON_SALE = (By.XPATH, "//option[text()='On Sale']")
    VERIFY_ON_SALE = (By.XPATH, "//div[text()='On sale']")

    def off_plan_btn(self):
        elements = self.driver.find_elements(*self.OFF_PLAN_BTN)
        sleep(3)
        if elements:
            first_element = elements[0]
            first_element.click()

            self.wait_until_clickable(*self.OFF_PLAN_BTN)
        else:
            print("No elements found")

    def off_plan_opens(self):
        self.find_element(*self.OFF_PLAN_OPENS)
        self.verify_text('Total projects', *self.OFF_PLAN_OPENS)

    def sales_status(self):
        self.find_element(*self.SALES_STATUS_BTN).click()

    def on_sale(self):
        self.find_element(*self.ON_SALE).click()

    def verify_on_sale(self):
        sleep(3)
        self.find_element(*self.VERIFY_ON_SALE)
        self.verify_text('On sale', *self.VERIFY_ON_SALE)








