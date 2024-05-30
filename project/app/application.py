from basepage import BasePage


class Application:
    def __init__(self, driver):
        self.base_page = BasePage(driver)
