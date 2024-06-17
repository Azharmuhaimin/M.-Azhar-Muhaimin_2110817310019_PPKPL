from selenium import webdriver
import unittest
from time import sleep
from login_page4 import LoginPage
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

    def test_interaksi(self):
        tab_beranda = self.driver.find_element(By.XPATH, "//a[@aria-label='Beranda']")
        tab_beranda.click()
        sleep(4)
        scroll_height = 435 
        scroll_script = f"window.scrollBy(0, {scroll_height});"
        self.driver.execute_script(scroll_script)
        sleep(4)
        suka_postingan = self.driver.find_element(By.XPATH, "//div[@aria-label='Suka'][@role='button']")
        suka_postingan.click() 
        sleep(5)
        dislike_postingan = self.driver.find_element(By.XPATH, "//div[@aria-label='Hapus Suka'][@role='button']")
        dislike_postingan.click()
        sleep(5)
        suka_postingan = self.driver.find_element(By.XPATH, "//div[@aria-label='Suka'][@role='button']")
        suka_postingan.click() 
        sleep(5)
        komen_postingan = self.driver.find_element(By.XPATH, "//div[@aria-label='Beri komentar'][@role='button']")
        komen_postingan.click()
        sleep(4)
        field_komentar = self.driver.find_element(By.XPATH, "//div[@aria-label='Tulis komentar...']")
        sleep(7)
        field_komentar.click()
        field_komentar.send_keys("mantap")
        sleep(4)
        field_komentar.send_keys(Keys.RETURN)
        sleep(4)


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
