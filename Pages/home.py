from selenium import webdriver
from selenium.webdriver.common.by import By
from browser import Driver


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.sidebar_locator = (By.CLASS_NAME, "css-hh3zui-sidebarContainer")
        self.home_locator = (By.CLASS_NAME, "css-gd7916-mainLogo")

    def is_at(self):
        try:
            self.driver.find_element(*self.sidebar_locator) # this triggers driver implicit wait, ensuring page loads
            current_url = self.driver.current_url
            if "admin" in current_url and "dashboard" in current_url:
                return True
            else:
                return False
        except: # if the sidebar isn't there, we are definitely not on the home page
            return False

    def goto(self, url):
        # todo: if(Login.LoggedOut()): Login().login(), use a static method to not require instance of login
        self.driver.find_element(*self.home_locator).click()
