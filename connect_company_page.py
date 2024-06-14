from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ConnectCompanyPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_on_menu(self):
        self.logger.info("Clicking on menu button")
        connect_button = self.find_element(By.CSS_SELECTOR, "div[class*='mobile-top-menu']")
        connect_button.click()

    def click_connect_company(self):
        self.logger.info("Attempting to click 'Connect the company' button")

        wait = WebDriverWait(self.driver, 15)

        try:
            # Find the element first
            connect_button = wait.until(
                 EC.visibility_of_element_located(
                     (By.XPATH, "/html/body/div[3]/div[2]/a[1]/div")
                 )
            )

            # Scroll into view
            self.driver.execute_script("arguments[0].scrollIntoView(true);", connect_button)

            # Click the element
            connect_button.click()
            self.logger.info("'Connect the company' button clicked")

        except Exception as e:
            self.logger.error(f"Error clicking 'Connect the company' button: {e}")
            self.logger.debug("Page source at the time of error:")
            self.logger.debug(self.driver.page_source)
            raise
