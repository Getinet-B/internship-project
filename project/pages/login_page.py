from basepage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def login(self, email, password):
        email_field = self.find_element(By.ID, 'email-2')
        password_field = self.find_element(By.ID, 'field')
        login_button = self.find_element(By.CSS_SELECTOR, "a[class*='login-button']")

        email_field.send_keys(email)
        password_field.send_keys(password)
        login_button.click()
        