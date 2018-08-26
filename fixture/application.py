from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.navigation import NavigationHelper
from fixture.manager import ManagerHelper



class Application_test_add_group:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
        self.navigation  = NavigationHelper(self)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def destroy(self):
        self.wd.quit()

class  Application_test_add_contact_in_book_address:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
        self.navigation = NavigationHelper(self)
        self.session = SessionHelper(self)
        self.manager = ManagerHelper(self)

    def destroy(self):
        self.wd.quit()