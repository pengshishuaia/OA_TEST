from selenium import webdriver
from .driver import browser
import unittest
import os

class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()