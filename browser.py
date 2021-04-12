from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Driver:
    def __init__(self):

        browserOptions = Options()
        browserOptions.add_argument("--headless")
        browserOptions.add_argument("--window-size=1440, 900") # reduces headless race conditions
        self.driver = webdriver.Chrome(options=browserOptions)
        self.driver.implicitly_wait(10)

    def get_instance(self):
        return self.driver
