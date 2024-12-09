from selenium.webdriver.common.by import By

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        element.click()

    # def verify_page_title(self, expected_title):
    #     return self.driver.title == expected_title
    #
    # def type_into_element(self, locator_type, locator_value, text_to_enter):
    #     element = self.get_element(locator_type, locator_value)
    #     element.clear()
    #     element.send_keys(text_to_enter)

    def get_element(self, locator_type, locator_value):
        if locator_type == "id":
            return self.driver.find_element(By.ID, locator_value)
        elif locator_type == "name":
            return self.driver.find_element(By.NAME, locator_value)
        elif locator_type == "class_name":
            return self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_type == "link_text":
            return self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_type == "xpath":
            return self.driver.find_element(By.XPATH, locator_value)
        elif locator_type == "css":
            return self.driver.find_element(By.CSS_SELECTOR, locator_value)
        else:
            raise ValueError(f"Invalid locator type: {locator_type}")
