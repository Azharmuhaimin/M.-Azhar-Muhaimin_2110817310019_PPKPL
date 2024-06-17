from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.facebook.com/"
        self.email_field = (By.ID, "email")
        self.password_field= (By.ID, "pass")
        self.login_button = (By.NAME, "login")

    def masuk(self):
        self.driver.get(self.url)

    def set_email(self, email):
        email_input = self.driver.find_element(*self.email_field)
        email_input.clear()
        email_input.send_keys(email)

    def set_password(self, password):
        password_input = self.driver.find_element(*self.password_field)
        password_input.clear()
        password_input.send_keys(password)

    def click_login(self):
        login_button = self.driver.find_element(*self.login_button)
        login_button.click()

    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_login()

    def is_login_successful(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[@aria-label='Beranda']"))
            )
            return True
        except:
            return False
