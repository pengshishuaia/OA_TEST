import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from test_case.Login_Test import *


TestTest.test_user_login()
class test_mail(unittest.TestCase):

    send_email = (By.XPATH, "//span[contains(text(),'写 信')]")
    send_recipients = (By.XPATH, "//div[2]/div/input")
    send_title = (By.XPATH, "//div[2]/div/div/div/input")
    send_iframe = (By.CLASS_NAME, "APP-editor-iframe")
    send_content = (By.XPATH, "/html/body")

    def test_send_email(self):
        self.driver.find_element(*self.send_email).click()
    def test_send_recipients(self):
        self.driver.find_element(*self.send_recipients).send_keys("wxxps18910503484@126.com")
    def test_send_title(self):
        self.driver.find_element(*self.send_title).send_keys("33221212")
    def test_send_iframe(self):
        return self.driver.find_element(*self.send_iframe)
    def test_send_content(self):
        self.driver.find_element(*self.send_content).send_keys("ppppsss ")

    def send_Email(self):
        time.sleep(5)
        self.test_send_email()
        self.test_send_recipients()
        self.test_send_title()
        self.driver.switch_to.frame(self.test_send_iframe())
        self.test_send_content()

def send_test():
    po = test_mail()
    po.send_Email()
if __name__ == '__main__':
    unittest.main()


