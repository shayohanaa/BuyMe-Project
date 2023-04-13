from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from homepage import HomePage
from homepage import Login
from homepage import Extra
import json


class setUp(TestCase):
    def setUp(self):
        json_file = open('config.json', 'r')
        data = json.load(json_file)
        browser = data['browserType']
        if browser == 'chrome':
            self.driver = webdriver.Chrome(service=Service('<CHROMEDRIVER_PATH>'))
        elif browser == 'firefox':
            self.driver = webdriver.Firefox(service=Service('<FIREFOXDRIVER_PATH>'))

        url = data['url']
        self.driver.get(url)

        self.homepage = HomePage(self.driver)
        self.login = Login(self.driver)
        self.extras = Extra(self.driver)

    def test_BuyMe(self):
        self.driver.implicitly_wait(20)
        # self.homepage.signUp() # test turned off by default
        # self.login.Login() # test turned off by default
        self.login.fulfillGift()
        self.login.Gift()
        self.extras.Loading()
        self.extras.errorMessage()
        self.extras.giftScreen()
        self.extras.info_Screen()

    def tearDown(self):
        self.driver.quit()
