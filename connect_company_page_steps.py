from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


@given('Open the main page')
def open_main(context):
    context.app.home_page.open_main()


@when('Log in to the page')
def log_in_to_the_page(context):
    context.app.login_page.login('getinet12183@gmail.com', 'Gb12345678%/?')
    sleep(6)


@when('Click on “Connect the company”')
def click_connect_company(context):
    context.app.connect_company_page.click_connect_company()
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