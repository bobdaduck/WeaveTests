import unittest
import Pages.users

from Pages.users import UsersPage
from Pages.users import AddUsersPage
from Pages.home import HomePage
from Pages.login import LoginPage
from browser import Driver

class LoginTests(unittest.TestCase):

    def setUp(self):
        self.driver = Driver().get_instance()
        self.Login = LoginPage(self.driver)
        self.Home = HomePage(self.driver)
        self.AddUsersPage = AddUsersPage(self.driver)
        self.Login.login()

    def test_create_user(self):
        self.AddUsersPage.goto()
        self.AddUsersPage.add_user()  # default uses generator

    def tearDown(self):
        # self.driver.quit()
        pass


if __name__ == '__main__':
    unittest.main()
