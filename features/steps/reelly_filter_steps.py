from behave import given, when, then
from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page
from pages.main_page import MainPage


EMAIL_TAB = (By.CSS_SELECTOR, "[data-name='Email 2']")
PASSWORD = (By.CSS_SELECTOR, "[name='Password']")
LOG_IN_BTN = (By.CSS_SELECTOR, ".login-button")


@given('Open reelly main page')
def open_reelly(context):
    context.driver.get('https://soft.reelly.io/sign-in')


@given('Input email {email}')
def log_in(context, email):
    context.page = Page(context.driver)
    context.page.input_text("kesha0801@gmail.com", *EMAIL_TAB)
    sleep(2)
    context.page.input_text("Reelly@0801", *PASSWORD)
    sleep(2)
    context.page.wait_and_click(*LOG_IN_BTN)


@when('Click on “off plan” at the left side menu')
def off_plan_btn(context):
    context.main_page = MainPage(context.driver)
    context.main_page.off_plan_btn()


@then('Verify the right page opens')
def off_plan_opens(context):
    context.main_page = MainPage(context.driver)
    context.main_page.off_plan_opens()


@when('Click on Sales status')
def sales_status(context):
    context.main_page = MainPage(context.driver)
    context.main_page.sales_status()


@when('Filter by sale status of “On Sale”')
def on_sale(context):
    context.main_page = MainPage(context.driver)
    context.main_page.on_sale()


@then('Verify each product contains the "On Sale" tag')
def verify_on_sale(context):
    context.main_page = MainPage(context.driver)
    context.main_page.verify_on_sale()



























