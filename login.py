from selenium.webdriver.common.by import By
from Framework.values import URL
from Framework.values import EMAIL
from Framework.values import PASSWORD


# from browser import Driver

class Login:
    URL = "https://app.getweave.com/"

    def __init__(self, driver):
        # self.driver = Driver()
        # self.username = (By.CSS_SELECTOR, '[name="username"]') possible alternative way of doing this
        # defining selectors and then referencing find_by each time, we'll see what works better (if DOM reloads a lot)
        # we'd get a lot of stale element exceptions if we prefind elements a lot
        self.driver = driver.get_instance()
        self.username = driver.find_element(By.CSS_SELECTOR, '[name="username"]')
        self.password = driver.find_element(By.CSS_SELECTOR, '[name="password"]')
        self.submit = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')

    def goto(self):
        self.driver.get(URL)

    def is_at(self):
        if self.driver.current_url.contains("admin") and self.driver.current_url.contains("dashboard"):
            return True
        else:
            return False

    def login(self):
        if not self.is_at():  # anytime we use the login class, we're trying to do something on the login screen.
            self.goto()
        self.username.send_keys(EMAIL)
        self.password.send_keys(PASSWORD)
        self.submit.click()
