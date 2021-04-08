from selenium import webdriver
from selenium.webdriver.common.by import By
from browser import Driver

class Home:

    def __init__(self, driver):
        #self.driver = Driver()
        self.sidebar = self.driver.find_element(By.CLASS_NAME, "css-hh3zui-sidebarContainer")
        self.homeLogo = self.driver.find_element(By.CLASS_NAME, "css-gd7916-mainLogo")


    def is_at(self):
        if self.driver.url.contains("admin") and self.driver.url.contains("dashboard"):
            return True
        else:
            return False

    def goto(self, url):
        if isinstance(url, str):
            #later: if(Pages.LoggedOut()): Login().login()
            self.homeLogo.click()
        else:
            raise TypeError("URL must be a string.")