from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ConnectCompanyPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_connect_company(self):
        connect_button = self.find_element(By.XPATH, "//*[text()='Connect the company']")
        connect_button.click()
