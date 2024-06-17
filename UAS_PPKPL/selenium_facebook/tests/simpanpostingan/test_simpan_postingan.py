from selenium import webdriver
import unittest
from time import sleep
from login_page5 import LoginPage
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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

    def test_simpan_postingan(self):
        tab_beranda = self.driver.find_element(By.XPATH, "//a[@aria-label='Beranda']")
        tab_beranda.click()
        sleep(4)
        scroll_height = 435 
        scroll_script = f"window.scrollBy(0, {scroll_height});"
        self.driver.execute_script(scroll_script)
        sleep(4)
        simpan_postingan = self.driver.find_element(By.XPATH, "//div[@aria-label='Tindakan untuk postingan ini'][@role='button']")
        simpan_postingan.click()
        sleep(4)
        simpan_button = self.driver.find_element(By.XPATH, '//span[text()="Simpan postingan"]')
        simpan_button.click()
        sleep(5)
        pilih_tempat = self.driver.find_element(By.XPATH, "//div[@aria-label='Selesai'][@role='button']")
        pilih_tempat.click()
        sleep(5)
        tersimpan = self.driver.find_element(By.XPATH, '//span[text()="Tersimpan"]')
        tersimpan.click()
        sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()