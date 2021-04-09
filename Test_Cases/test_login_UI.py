import unittest

from Pages.home import HomePage
from Pages.login import LoginPage
from browser import Driver


class LoginTests(unittest.TestCase):

    def setUp(self):  # run before all tests in file
        self.driver = Driver().get_instance()
        self.Login = LoginPage(self.driver)
        self.Home = HomePage(self.driver)

    def test_login_UI(self):
        self.Login.goto()  # redundant due to "catch: goto()" in login method, but this makes test steps clearer
        self.Login.login()  # no arguments = default credentials pulled from env
        assert self.Home.is_at()  # login successful!

    def test_login_UI_bad(self):
        self.Login.goto()
        self.Login.login(password_to_send="an incorrect password")
        assert self.Home.is_at() is False

    def test_login_api(self):
        
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
