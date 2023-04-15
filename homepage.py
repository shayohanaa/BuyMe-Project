from selenium.webdriver.common.by import By
from base_page import BasePage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import json
import allure


class Constants:
    User = "shayohanaa@gmail.com"
    Pass = "12345678Aa"


class HomePage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def signUp(self):
        self.click_element(By.XPATH, '//*[@id="ember1006"]/div/ul[1]/li[3]/a')
        self.click_element(By.XPATH, "//div[1]/div/div/div[3]/div[1]/span")
        self.enter_text(By.ID, 'ember1879', 'Shay')
        self.enter_text(By.ID, 'ember1886', Constants.User)
        self.enter_text(By.ID, 'valPass', Constants.Pass)
        self.enter_text(By.ID, 'ember1900', Constants.Pass)
        self.click_element(By.CLASS_NAME, 'fill')
        self.click_element(By.ID, 'ember1910')
        name = self.find_element(By.ID, 'ember1879').text
        assert name == "John Doe"


class Login(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def Login(self):
        self.click_element(By.XPATH, '//header/div[1]/div/ul[1]/li[3]')
        self.enter_text(By.CSS_SELECTOR, 'input[type=email]', Constants.User)
        self.enter_text(By.CSS_SELECTOR, 'input[type=password]', Constants.Pass)
        self.click_element(By.CSS_SELECTOR, 'button[type=submit]')

    def fulfillGift(self):
        self.wait(By.ID, 'ember1053', 15)
        self.click_element(By.ID, 'ember1053')
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable((By.ID, "ember1076")))
        self.click_element(By.ID, 'ember1076')

        self.click_element(By.ID, 'ember1088')
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable((By.ID, 'ember1111')))
        self.click_element(By.ID, 'ember1111')

        self.click_element(By.ID, 'ember1120')
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable((By.ID, "ember1171")))
        self.click_element(By.ID, 'ember1171')

        allure.attach(self.driver.get_screenshot_as_png(), name="homepage", attachment_type=allure.attachment_type.PNG)
        self.click_element(By.ID, 'ember1199')

    def Gift(self):
        self.wait(By.PARTIAL_LINK_TEXT, 'Claro', 10)
        allure.attach(self.driver.get_screenshot_as_png(), name="Type", attachment_type=allure.attachment_type.PNG)
        get_url = self.driver.current_url
        print(get_url)
        assert get_url == "https://buyme.co.il/search?budget=1&category=438&region=13"
        self.click_element(By.PARTIAL_LINK_TEXT, "Claro")
        self.driver.implicitly_wait(2)
        self.enter_text(By.CSS_SELECTOR, 'input[inputmode=decimal]', '150')
        allure.attach(self.driver.get_screenshot_as_png(), name="Gift", attachment_type=allure.attachment_type.PNG)
        self.click_element(By.CSS_SELECTOR, 'button[type=submit]')
        self.click_element(By.XPATH, '//form/div[1]/div/div/div/div/div[1]')
        self.enter_text(By.ID, 'friendName', 'John Doe')
        self.click_element(By.CLASS_NAME, 'selected-name')
        WebDriverWait(self.driver, 2).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//form/div[2]/div[2]/label/div/div[2]/ul/li[2]")))
        self.click_element(By.XPATH, '//form/div[2]/div[2]/label/div/div[2]/ul/li[2]')
        self.scroll_down_end()
        self.clear_text(By.XPATH, '//form/div[2]/div[4]/label/textarea')
        self.enter_text(By.XPATH, '//form/div[2]/div[4]/label/textarea', 'Happy birthday.')
        self.driver.find_element(By.CSS_SELECTOR, "input[name=logo]").send_keys("C:\\Users\\shayo\\passover.png")
        allure.attach(self.driver.get_screenshot_as_png(), name="Blessings", attachment_type=allure.attachment_type.PNG)
        self.driver.implicitly_wait(5)
        self.click_element(By.CSS_SELECTOR, 'button[type=submit]')
        self.click_element(By.CSS_SELECTOR, 'div[gtm=עכשיו')
        self.click_element(By.CSS_SELECTOR, 'svg[gtm=method-email')
        self.enter_text(By.CSS_SELECTOR, 'input[name=email]', 'JohnDoe@gmail.com')
        self.scroll_down_end()
        self.enter_text(By.CSS_SELECTOR, 'input[type=text]', 'John Doe')
        allure.attach(self.driver.get_screenshot_as_png(), name="Receiver", attachment_type=allure.attachment_type.PNG)
        # self.assert_Text(By.CSS_SELECTOR, 'input[type=text]', 'John Doe')
        self.driver.get("https://buyme.co.il")


class Extra(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def Loading(self):
        element = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div')
        height = element.size['height']
        width = element.size['width']
        print(f'\nElement height: {height}px')
        print(f'Element width: {width}px')

    def errorMessage(self):
        self.wait(By.XPATH, '//header/div[1]/div/ul[1]/li[3]', 10)
        self.click_element(By.XPATH, '//header/div[1]/div/ul[1]/li[3]')
        self.click_element(By.XPATH, '//form/button')
        self.assert_Text(By.CLASS_NAME, 'parsley-required', 'כל המתנות מחכות לך! אבל קודם צריך מייל וסיסמה')

    def giftScreen(self):
        self.driver.get("https://buyme.co.il")
        self.wait(By.ID, 'ember1053', 5)
        self.click_element(By.ID, 'ember1053')
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable((By.ID, "ember1076")))
        self.click_element(By.ID, 'ember1076')

        self.click_element(By.ID, 'ember1088')
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable((By.ID, 'ember1111')))
        self.click_element(By.ID, 'ember1111')

        self.click_element(By.ID, 'ember1120')
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable((By.ID, "ember1171")))
        self.click_element(By.ID, 'ember1171')
        self.scroll_down_end()
        allure.attach(self.driver.get_screenshot_as_png(), name="giftScreen", attachment_type=allure.attachment_type.PNG)

    def info_Screen(self):
        self.driver.get("https://buyme.co.il/money/1229712?price=150")
        element = self.driver.find_element(By.CLASS_NAME, 'bottom-xs')
        color = element.value_of_css_property('color')
        print("The element color is: ", color)
