import unittest
from selenium import webdriver

class Selenium(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r'')
