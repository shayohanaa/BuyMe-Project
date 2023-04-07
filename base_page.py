from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator_type, locator_value):
        self.driver.find_element(locator_type, locator_value).click()

    def find_element(self, locator_type, locator_value):
        self.driver.find_element(locator_type, locator_value)

    def wait(self, locator_type, locator_value, sec):
        WebDriverWait(self.driver, sec).until(
            expected_conditions.presence_of_element_located((locator_type, locator_value)))

    def scroll_down_end(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_up_end(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    def clear_text(self, locator_type, locator_value):
        self.driver.find_element(locator_type, locator_value).clear()

    def enter_text(self, locator_type, locator_value, text):
        self.driver.find_element(locator_type, locator_value).send_keys(text)

    def assert_Text(self, locator_type, locator_value, asserting_text):
        text = self.driver.find_element(locator_type, locator_value).text
        assert text == asserting_text
