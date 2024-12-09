import time

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utilities import ConfigReader

def before_scenario(context, driver):
    # Read browser name from configuration
    browser_name = ConfigReader.read_configuration("basic info", "browser")

    if browser_name == "chrome":
        service = Service("drivers/chromedriver")  # Specify the correct path
        context.driver = webdriver.Chrome(service=service)
    elif browser_name == "firefox":
        service = Service("drivers/geckodriver")  # Specify the correct path for Firefox
        context.driver = webdriver.Firefox(service=service)
    elif browser_name == "edge":
        service = Service("drivers/edgedriver")  # Specify the correct path for Edge
        context.driver = webdriver.Edge(service=service)
    
    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_configuration("basic info", "ui_url"))


def after_scenario(context, scenario):
    # Quit the driver only if it exists
    if hasattr(context, "driver") and context.driver:
        context.driver.quit()


def after_step(context, step):
    # Attach a screenshot for failed steps
    if step.status == "failed" and hasattr(context, "driver") and context.driver:
        allure.attach(context.driver.get_screenshot_as_png(),
                      name="failed_screenshot",
                      attachment_type=AttachmentType.PNG)
