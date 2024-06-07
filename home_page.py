from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://soft.reelly.io/sign-in'

    def open_main(self):
        print("HomePage open method called")
        super().open(self.url)
