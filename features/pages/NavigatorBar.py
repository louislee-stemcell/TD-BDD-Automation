from features.pages.BasePage import BasePage

class NavigatorBar(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
    
    hamburger_xpath = "//button[@phx-value-target='navigation']//*[name()='svg']"
    run_control_xpath = "//a[normalize-space()='Run Control']"
    protocol_xpath = "//a[normalize-space()='Protocol']"
    online_library_xpath = "//a[normalize-space()='Online Library']"
    history_xpath = "//a[normalize-space()='History']"
    settings_xpath = "//a[normalize-space()='Settings']"
    
    def click_hamburger_icon(self):
        self.click_on_element("xpath", self.hamburger_xpath)

    
    def is_run_control_screen_button_displayed(self):
        run_control = self.get_element("xpath", self.run_control_xpath)
        return run_control.is_displayed()
