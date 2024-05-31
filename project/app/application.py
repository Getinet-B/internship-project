from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.connect_company_page import ConnectCompanyPage


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(driver)
        self.home_page = HomePage(driver)
        self.login_page = LoginPage(driver)
        self.connect_company_page = ConnectCompanyPage(driver)

