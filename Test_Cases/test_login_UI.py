import unittest

from Framework.Pages.home import Home
from Framework.Pages.login import Login
from browser import Driver


class LoginTests(unittest.TestCase):

    def setUp(self): #run before all tests in file
        self.driver = Driver()
        self.Login = Login(self.driver)
        self.Home = Home(self.driver)

    def test_login_UI(self):
        Login.load()
        Login.login()
        assert (Home.isAt)  # login successful!

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()
