from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open the main page')
def open_page(context):
    context.driver.get('https://soft.reelly.io/sign-in')


@when('Log in to the page')
def log_in_to_the_page(context):
    email_field = context.driver.find_element(By.ID, 'email-2')
    password_field = context.driver.find_element(By.ID, 'field')
    email_field.send_keys('getinet12183@gmail.com')  # Replace with your email
    password_field.send_keys('Gb12345678%/?')  # Replace with your password
    context.driver.find_element(By.CSS_SELECTOR, "a[class*='login-button']").click()
    sleep(6)


@when('Click on “Connect the company”')
def click_connect_company(context):
    context.driver.find_element(By.XPATH, "//*[text()='Connect the company']").click()
    sleep(6)


@when('Switch to the new tab')
def switch_to_new_tab(context):
    handles = context.driver.window_handles
    context.driver.switch_to.window(handles[-1])
    sleep(3)


@then('Verify the right tab opens')
def verify_right_tab_opens(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[text()='Get details about Reelly corporate offer']").text
    assert "Get details about Reelly corporate offer" in actual_text, f'Error! Text "Get details about Reelly corporate offer" not in {actual_text}'
