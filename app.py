from selenium import webdriver
from email_data import EMAIL_LOGIN, EMAIL_PASSWORD
import time


class ChromeAuto:
    def __init__(self):
        self._email_login = EMAIL_LOGIN
        self._email_password = EMAIL_PASSWORD
        self.driver = webdriver.Chrome('./chromedriver/chromedriver')

    @property
    def email_login(self):
        return self._email_login

    @property
    def email_password(self):
        return self._email_password

    def open_browser(self):
        self.driver.get('https://outlook.live.com/owa/')

    def signin(self):
        try:
            self.btn_signin_click()
            self.put_email_login()
            self.put_email_password()

        except Exception as e:
            print(e)

    def btn_signin_click(self):
        time.sleep(1)
        self.driver.find_element_by_link_text('Sign in').click()

    def put_email_login(self):
        time.sleep(1)
        self.driver.find_element_by_name('loginfmt').send_keys(self.email_login)
        time.sleep(1)
        self.driver.find_element_by_id('idSIButton9').click()
        time.sleep(1)
        self.check_email_login()

    def put_email_password(self):
        time.sleep(1)
        self.driver.find_element_by_name('passwd').send_keys(self.email_password)
        time.sleep(1)
        self.driver.find_element_by_id('idSIButton9').click()
        time.sleep(1)
        self.check_email_password()

        if len(self.driver.find_elements_by_id('KmsiDescription')) > 0:
            self.check_staysignedin()

    def check_staysignedin(self):

        time.sleep(2)

        try:

            btn_yes = self.driver.find_element_by_id('idSIButton9')
            btn_no = self.driver.find_element_by_id('idBtn_Back')

            btn_no.click()
        except Exception as e:
            raise Exception('An unknown error has occurred.')

    def check_email_login(self):

        username_error = self.driver.find_elements_by_id('usernameError')

        if len(username_error) > 0:
            raise Exception('Incorrect username.')

    def check_email_password(self):

        password_error = self.driver.find_elements_by_id('passwordError')

        if len(password_error) > 0:
            raise Exception('Incorrect password.')
        


    
        




        