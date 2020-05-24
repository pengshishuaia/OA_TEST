#!/usr/bin/env python
# _*_coding:utf-8_*_
# Author:Vincent Lan
import unittest, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class QQ_mail(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://mail.126.com"

    def test_mail_login(self):
        """QQ邮箱登录"""
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url + "/")

        driver.find_element(By.ID, "lbNormal").click()
        driver.switch_to.frame("")
        driver.find_element(By.NAME, "email").send_keys("wxxps18910503484 ")
        driver.find_element(By.NAME, "password").send_keys("wowangle23")
        driver.find_element(By.ID, "dologin").click()
        time.sleep(5)
        driver.find_element_by_xpath("//span[contains(text(),'写 信')]").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//div[2]/div/input").send_keys("wxxps18910503484@126.com")
        driver.find_element(By.XPATH, "//div[2]/div/div/div/input").send_keys("测试内容")
        xpath = driver.find_element(By.CLASS_NAME, "APP-editor-iframe")
        driver.switch_to.frame(xpath)
        driver.find_element(By.XPATH,"/html/body").send_keys("ppppppssss")


"""
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
"""
if __name__ == "__main__":
    unittest.main()