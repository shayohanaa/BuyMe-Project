from selenium.webdriver.common.by import By
from base_page import BasePage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
import json
import allure


class Constants:
    User = "shayohanaa@gmail.com"
    Pass = "12345678Aa"


class HomePage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        json_file = open('config.json', 'r')
        data = json.load(json_file)
        url = data['url']
        self.driver.get(url)

    def signUp(self):
        self.click_element(By.XPATH, '//*[@id="ember1006"]/div/ul[1]/li[3]/a')
        self.click_element(By.XPATH, "//div[1]/div/div/div[3]/div[1]/span")
        self.enter_text(By.ID, 'ember1879', 'Shay')
        self.enter_text(By.ID, 'ember1886', Constants.User)
        self.enter_text(By.ID, 'valPass', Constants.Pass)
        self.enter_text(By.ID, 'ember1900', Constants.Pass)
        self.click_element(By.CLASS_NAME, 'fill')
        self.click_element(By.ID, 'ember1910')
        name = self.find_element(By.ID, 'ember1879')
        assert name == "John Doe"


class Login(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        json_file = open('config.json', 'r')
        data = json.load(json_file)
        url = data['url']
        self.driver.get(url)

    def Login(self):
        self.click_element(By.XPATH, '//*[@id="ember1006"]/div/ul[1]/li[3]/a')
        self.enter_text(By.ID, 'ember1852', Constants.User)
        self.enter_text(By.ID, 'ember1859', Constants.Pass)
        self.click_element(By.ID, 'ember1868')

    def fulfillGift(self):
        self.wait(By.ID, 'ember1053', 10)
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
        # get_url = self.driver.current_url
        # assert get_url == "https://buyme.co.il/search?category=438&region=11"
        self.click_element(By.PARTIAL_LINK_TEXT, "Claro")
        self.driver.implicitly_wait(2)
        self.enter_text(By.CSS_SELECTOR, 'input[inputmode=decimal]', '150')
        allure.attach(self.driver.get_screenshot_as_png(), name="Gift", attachment_type=allure.attachment_type.PNG)
        self.click_element(By.CSS_SELECTOR, 'button[type=submit]')
        self.click_element(By.XPATH, '//form/div[1]/div/div/div/div/div[1]')
        self.enter_text(By.ID, 'friendName', 'John Doe')
        self.click_element(By.CLASS_NAME, 'selected-name')
        time.sleep(3)
        self.driver.implicitly_wait(2)
        # self.wait(By.CSS_SELECTOR, 'li[value=10]', 10)
        self.click_element(By.XPATH, '//form/div[2]/div[2]/label/div/div[2]/ul/li[2]')
        self.scroll_down_end()
        self.clear_text(By.XPATH, '//form/div[2]/div[4]/label/textarea')
        self.enter_text(By.XPATH, '//form/div[2]/div[4]/label/textarea', 'Happy birthday.')
        allure.attach(self.driver.get_screenshot_as_png(), name="Blessings", attachment_type=allure.attachment_type.PNG)
#####
        # self.click_element(By.XPATH, '//form/div[2]/div[5]/div[2]/div[1]/label')
        # time.sleep(1)
        # self.upload_File(By.XPATH, '//form/div[2]/div[5]/div[2]/div[1]/label', "C:/Users/shayo/passover.jpg")
        # time.sleep(1)
#####
        self.click_element(By.CSS_SELECTOR, 'button[type=submit]')
        # self.click_element(By.ID, 'ember3380')
        self.click_element(By.CSS_SELECTOR, 'svg[gtm=method-email')
        self.enter_text(By.CSS_SELECTOR, 'input[name=email]', 'JohnDoe@gmail.com')
        self.scroll_down_end()
        self.enter_text(By.CSS_SELECTOR, 'input[type=text]', 'John Doe')
        allure.attach(self.driver.get_screenshot_as_png(), name="Receiver", attachment_type=allure.attachment_type.PNG)
        time.sleep(3)

        # receiver = self.find_element(By.CSS_SELECTOR, 'input[type=text]')
        # assert receiver == "John Doe"


class Extras(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def Loading(self):
        json_file = open('config.json', 'r')
        data = json.load(json_file)
        url = data['url']
        self.driver.get(url)

        element = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div')

        height = element.size['height']
        width = element.size['width']

        print(f'\nElement height: {height}px')
        print(f'Element width: {width}px')

