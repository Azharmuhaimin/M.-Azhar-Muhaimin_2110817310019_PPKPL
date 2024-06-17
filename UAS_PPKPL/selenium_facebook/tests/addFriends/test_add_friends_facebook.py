from selenium import webdriver
import unittest
from time import sleep
from login_page3 import LoginPage
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
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

    def test_melakukan_pencarian_orang(self):
        field_pencarian = self.driver.find_element(By.XPATH, "//input[@type='search']")
        field_pencarian.click()
        field_pencarian.send_keys("Azhar Muhaimin")
        field_pencarian.send_keys(Keys.RETURN)
        sleep(4)
        tab_orang = self.driver.find_element(By.XPATH, "//a[contains(@href,'people')]")
        tab_orang.click()
        self.assertTrue(self.login_page.apakah_berhasil_mencari_orang(), "Berhasil mencari orang")
        sleep(3)
        hasil_pencarian= self.driver.find_element(By.XPATH, "//div[@aria-label='Hasil Pencarian']")
        hasil_pencarian.click()
        scroll_height = 100 
        scroll_script = f"window.scrollBy(0, {scroll_height});"
        self.driver.execute_script(scroll_script)
        sleep(4)
        first_result = self.driver.find_element(By.XPATH, "//a[contains(@href,'azhar')]")
        first_result.click()
        sleep(3)
        tambah_teman = self.driver.find_element(By.XPATH, ("//*[contains(text(), 'Tambahkan teman')]"))
        tambah_teman.click()
        self.assertTrue(self.login_page.apakah_berhasil_menambah_teman(), "Berhasil mengirim permintaan")
        sleep(3)
        batal_teman = self.driver.find_element(By.XPATH, ("//*[contains(text(), 'Batalkan Permintaan')]"))
        batal_teman.click()
        self.assertTrue(self.login_page.apakah_membatalkan_permintaan(), "Berhasil membatalkan permintaan")
        sleep(7)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
