from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Driver:
    def __init__(self):

        browserOptions = Options()
        # browserOptions.add_argument("--headless")

        self.driver = webdriver.Chrome(options=browserOptions)
        self.driver.implicitly_wait(7)

    def get_instance(self):
        return self.driver
