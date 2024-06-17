from selenium import webdriver
import unittest
from time import sleep
from login_page2 import LoginPage
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
   
class AddFriends(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.set_preference("dom.webdriver.enabled", False)
        options.set_preference("useAutomationExtension", False)
        self.driver = webdriver.Firefox(options=options)
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.login_page.masuk()
        self.login_page.login("muhaiminazhar6@gmail.com", "muhaimin098")
        sleep(5)

    def test_pindah_tab(self):
        tab_teman = self.driver.find_element(By.XPATH, "//a[contains(@href,'friends')]")
        tab_teman.click()
        self.assertTrue(self.login_page.apakah_berhasil_pindah_teman(), "Berhasil mencari orang")
        sleep(4)
        tab_grup = self.driver.find_element(By.XPATH, "//a[contains(@href,'groups')]")
        tab_grup.click()
        self.assertTrue(self.login_page.apakah_berhasil_pindah_grup(), "Berhasil mencari orang")
        sleep(4)
        tab_beranda = self.driver.find_element(By.XPATH, "//a[@aria-label='Beranda']")
        tab_beranda.click()
        self.assertTrue(self.login_page.apakah_berhasil_pindah_beranda(), "Berhasil mencari orang")
        sleep(4)  

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
