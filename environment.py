from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

from app.application import Application
from support.logger import logger


def browser_init(context, scenario_name):
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.wait = WebDriverWait(context.driver, timeout=15)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)
    context.home_page = context.app.home_page


def before_step(context, step):
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        logger.warning(f'Step failed: {step}')
        # context.app.base_page.save_screenshot(step)


def after_scenario(context, feature):
    context.driver.quit()
