from selenium.webdriver.common.by import By
import random

FIRST_NAMES = ["Aaron", "Alfred", "Arnold", "Albert", "Adrian"]
LAST_NAMES = ["Smith", "Smythe", "Smitt", "Smitch", "Sith"]
JOB_TITLES = ["Owner", "Front Desk", "Office Manager", "Doctor/Practicioner", "Doctor/Practitioners Assistant (Hygienist, Dental/Opto/Other assistant, etc.)", "Back Office"]
ROLES = ["Admin", "Advanced Team Member", "Payment Admin", "Payment - Data Exporting", "Payments - Refunds", "Team Member"]

class UsersPage:

    def __init__(self, driver):
        self.driver = driver
        self.accounts_sidebar_locator = (By.CLASS_NAME, "css-1yonxha-menu-item-sidebarMenuItem")
        self.users_locator = (By.CLASS_NAME, "css-1yonxha-menu-item-sidebarMenuItem")

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
        self.driver.find_element(*self.accounts_sidebar_locator).click()
        self.driver.find_element(*self.users_locator).click()

    def add_user(userdata):
        pass

class AddUsersPage:
    def __init__(self, driver):
        self.mobile_access_locator = (By.ID, "field-f0a036")

class NewUserData:
    def __init__(self):
        self.first_name
        self.last_name
        self.job_title
        self.roles
        self.mobile_access  # true or false

class NewUserGenerator:
    def __init__(self, driver):

    @staticmethod
    def newUser():
        user_data = NewUserData()

        random_firstname = random.randint(0, len(FIRST_NAMES) - 1)
        user_data.first_name = FIRST_NAMES[random_firstname]

        random_lastname = random.randint(0, len(LAST_NAMES) - 1)
        user_data.last_name = LAST_NAMES[random_lastname]

        random_joblist = random.sample(JOB_TITLES, 3)
        user_data.job_title = JOB_TITLES[random_joblist]

        random_rolelist = random.sample(ROLES, 3)
        user_data.roles = ROLES[random_rolelist]

        random_mobileAccess = random.randint(0, 1)
        user_data.mobile_access = random_mobileAccess

        print(random.sample(ROLES, 3))  # multiple without duplicates

