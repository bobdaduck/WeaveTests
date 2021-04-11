from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Pages.variables import EMAIL_FOR_GENERATOR
import random
from Pages.helpers import find_element_by_class_then_text
from Pages.helpers import try_clicking_for_duration
from selenium.webdriver.common.action_chains import ActionChains
import time

FIRST_NAMES = ["Aaron", "Alfred", "Arnold", "Albert", "Adrian"]
LAST_NAMES = ["Smith", "Smythe", "Smitt", "Smitch", "Sith"]
JOB_TITLES = ["Owner", "Front Desk", "Office Manager", "Doctor/Practicioner",
              "Doctor/Practitioners Assistant (Hygienist, Dental/Opto/Other assistant, etc.)", "Back Office"]
ROLES = ["Admin", "Advanced Team Member", "Payment Admin", "Payment - Data Exporting", "Payments - Refunds",
         "Team Member"]


class UsersPage:

    def __init__(self, driver):
        self.driver = driver
        self.active_sidebar_locator = (By.CLASS_NAME, "css-12vigwj-SvgIcon")

    @staticmethod
    def get_accounts_sidebar_locator(driver):  # methods instead of properties keep code from automatically executing
        return find_element_by_class_then_text(driver, "css-rld5tt", "Account")

    @staticmethod
    def get_users_locator(driver):
        return find_element_by_class_then_text(driver, "css-rld5tt", "Users")

    def is_at(self):
        self.driver.find_element(*self.sidebar_locator)  # this triggers driver implicit wait, ensuring page loads
        current_url = self.driver.current_url
        if "employees" in current_url and "employee-list" in current_url:
            return True
        else:
            return False

    def goto(self):
        # todo: if(Login.LoggedOut()): Login().login(), use a static method to not require instance of login

        self.get_accounts_sidebar_locator(self.driver).click()
        self.driver.find_element(*self.active_sidebar_locator)  # implicit wait is better than thread.sleep()
        self.get_users_locator(self.driver).click()


class NewUserData:
    def __init__(self):
        email = ""
        first_name = ""
        last_name = ""
        job_titles = ""
        roles = ""
        mobile_access = 0  # true or false


class NewUserGenerator:

    @staticmethod
    def newUser():
        user_data = NewUserData()

        random_email_number = random.randint(0,
                                             1000)  # i.e gmail routes all youremail+x@gmail.com to youremail@gmail.com
        user_data.email = EMAIL_FOR_GENERATOR.replace('{rnd}', str(random_email_number))

        random_firstname = random.randint(0, len(FIRST_NAMES) - 1)
        user_data.first_name = FIRST_NAMES[random_firstname]

        random_lastname = random.randint(0, len(LAST_NAMES) - 1)
        user_data.last_name = LAST_NAMES[random_lastname]

        user_data.job_titles = random.sample(JOB_TITLES, 3)

        user_data.roles = random.sample(ROLES, 3)

        random_mobile_Access = random.randint(0, 1)  # python can cast 0 or 1 as bool
        user_data.mobile_access = random_mobile_Access

        return user_data


class AddUsersPage:
    def __init__(self, driver):
        self.driver = driver
        self.mobile_access_locator = (By.ID, "field-f0a036")
        self.add_user_button_locator = (By.CLASS_NAME, "css-1glk65-PrimaryButton")
        self.email_field = (By.ID, "email")
        self.firstname_locator = (By.CSS_SELECTOR, '[name="FirstName"]')
        self.lastname_locator = (By.CSS_SELECTOR, '[name="LastName"]')
        #self.job_dropdown_locator = (By.ID, "cd583f")
        #self.role_dropdown_locator = (By.ID, "2b60da")
        self.mobile_toggle_locator = (By.CSS_SELECTOR, '[name="MobileAccess"]')
        self.submit_locator = (By.CSS_SELECTOR, '[type="submit"]')

    def get_job_dropdown(self):
        # return self.driver.find_elements_by_class_name("css-e61m0h-DropdownInput-MultiselectInput")[0]
        return self.driver.find_element(By.CSS_SELECTOR, '[name="JobTitles"]')
    def get_roles_dropdown(self):
        return self.driver.find_elements_by_class_name("css-e61m0h-DropdownInput-MultiselectInput")[1]

    def add_user(self, userdata=NewUserGenerator.newUser()):
        if not self.is_at():
            self.goto()

        self.driver.find_element(*self.email_field).send_keys(userdata.email)
        try_clicking_for_duration(self.driver.find_element(*self.submit_locator), 5)
        self.driver.find_element(*self.firstname_locator).send_keys(userdata.first_name)
        self.driver.find_element(*self.lastname_locator).send_keys(userdata.last_name)
        actions = ActionChains(self.driver)  # actionchains is necessary due to Weave's custom dropdown classes
        actions.move_to_element(self.get_job_dropdown())
        actions.click()
        actions.perform()
        time.sleep(10)

        self.driver.find_element(By.ID, "cd583f-Office Manager")
        job_dropdown = Select(self.get_job_dropdown())
        for job in userdata.job_titles:
            job_dropdown.select_by_value(job)
        roles_dropdown = Select(self.get_roles_dropdown())
        for role in userdata.roles:
            roles_dropdown.select_by_value(role)
        if userdata.mobile_access:
            self.driver.find_element(*self.mobile_toggle_locator).click()

        self.driver.find_element(*self.submit_locator).click()

    def is_at(self):
        current_url = self.driver.current_url
        if "invite" in current_url and "employees" in current_url:
            return True
        else:
            return False

    def goto(self):
        users = UsersPage(self.driver)
        users.goto()
        self.driver.find_element(*self.add_user_button_locator).click()
