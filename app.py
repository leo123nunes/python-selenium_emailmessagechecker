from selenium import webdriver
from email_data import EMAIL_LOGIN, EMAIL_PASSWORD

class ChromeAuto:
    def __init__(self):
        self._email_login = EMAIL_LOGIN
        self._email_password = EMAIL_PASSWORD
        self.driver = webdriver.Chrome('./chromedriver/chromedriver')

    def open_browser(self):
        self.driver.get('https://www.google.com.br/')

        