import unittest
from selenium import webdriver
from login_page import LoginPage
from selenium.webdriver.firefox.options import Options
from time import sleep

class TestLogin(unittest.TestCase): 

    def setUp(self):
        options = Options()
        options.set_preference("dom.webdriver.enabled", False)
        options.set_preference("useAutomationExtension", False)
        self.driver = webdriver.Firefox(options=options)
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)

    def test_login_berhasil(self):
        self.login_page.masuk()
        self.login_page.login("muhaiminazhar6@gmail.com", "muhaimin098")
        sleep(5)
        self.assertTrue(self.login_page.is_login_successful(), "Login berhasil")

    def test_login_gagal(self):
        self.login_page.masuk()
        self.login_page.login("emailsalah633@gmail.com", "muhaimin098")
        self.assertFalse(self.login_page.is_login_successful(), "Login gagal karena salah email")

    def test_login_gagal2(self):
        self.login_page.masuk()
        self.login_page.login("", "")
        self.assertFalse(self.login_page.is_login_successful(), "Login gagal karena tidak mengisi email dan password")

    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()