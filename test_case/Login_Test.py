import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from test_case import initialization


class TestTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://mail.126.com"
        self.driver.get(self.base_url)
        #driver = self.driver

    loginname_loc = (By.ID, 'lbNormal')
    username_loc = (By.NAME, 'email')
    password_loc = (By.NAME, 'password')
    submit_loc = (By.ID, 'dologin')

    def loginname(self):
        self.driver.find_element(*self.loginname_loc).click()

    def type_username(self):
        self.driver.find_element(*self.username_loc).send_keys("wxxps18910503484")

    def type_password(self):
        self.driver.find_element(*self.password_loc).send_keys("wowangle23")

    def submit(self):
        self.driver.find_element(*self.submit_loc).click()

    def test_user_login(self):
        time.sleep(3)
        self.loginname()
        self.driver.switch_to.frame('')
        self.type_username()
        self.type_password()
        self.submit()

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

def login_test():
    po = TestTest()
    po.test_user_login()

# if __name__ == '__main__':
#     unittest.main()