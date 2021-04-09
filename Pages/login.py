from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
from Pages.variables import EMAIL
from Pages.variables import PASSWORD


# from browser import Driver


class LoginPage:

    def __init__(self, driver):
        # self.driver = Driver()
        # self.username = (By.CSS_SELECTOR, '[name="username"]') possible alternative way of doing this
        # defining selectors and then referencing find_by each time, we'll see what works better (if DOM reloads a lot)
        # we'd get a lot of stale element exceptions if we pre-find elements a lot
        self.login_url = "https://app.getweave.com/admin/login"

        self.driver = driver
        self.username_locator = (By.CSS_SELECTOR, '[name="username"]')
        self.password_locator = (By.CSS_SELECTOR, '[name="password"]')
        self.submit_locator = (By.CSS_SELECTOR, '[type="submit"]')
        self.provided_email = EMAIL
        self.provided_password = PASSWORD
        # self.username = driver.find_element(By.CSS_SELECTOR, '[name="username"]')
        # self.password = driver.find_element(By.CSS_SELECTOR, '[name="password"]')
        # self.submit = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')

    def goto(self):
        self.driver.get(self.login_url)

    def is_at(self):
        current_url = self.driver.current_url
        if "admin" in current_url and "login" in current_url:
            return True
        else:
            return False

    def login(self, email_to_send=EMAIL, password_to_send=PASSWORD):
        if not self.is_at():  # anytime we use the login class, we're trying to do something on the login screen.
            self.goto()
        username_field = self.driver.find_element(*self.username_locator)
        username_field.send_keys(email_to_send)
        password_field = self.driver.find_element(*self.password_locator)
        password_field.send_keys(password_to_send)
        submit_button = self.driver.find_element(*self.submit_locator)
        submit_button.click()
