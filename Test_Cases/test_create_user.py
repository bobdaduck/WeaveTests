import unittest
import Pages.users

from Pages.users import UsersPage
from Pages.users import AddUsersPage
from Pages.users import NewUserGenerator
from Pages.home import HomePage
from Pages.login import LoginPage
from browser import Driver

class LoginTests(unittest.TestCase):

    def setUp(self):
        self.driver = Driver().get_instance()
        self.Login = LoginPage(self.driver)
        self.Home = HomePage(self.driver)
        self.UsersPage = UsersPage(self.driver)
        self.AddUsersPage = AddUsersPage(self.driver)
        self.Login.login()

    def test_create_user(self):
        self.AddUsersPage.goto()
        new_user_data = NewUserGenerator.newUser()
        self.AddUsersPage.add_user(new_user_data)  # default uses generator
        self.UsersPage.Invitations.goto()
        assert new_user_data.email in self.driver.page_source

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
