from selenium.webdriver.firefox.webdriver import WebDriver

class Application:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_css_selector("body").click()
        wd.find_element_by_name("user").send_keys("%s" % username)
        wd.find_element_by_name("pass").send_keys("%s" % password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def init_group_creation(self):
        wd = self.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()

    def fill_group_creation(self, settings_ancillary):
        wd = self.wd
        wd.find_element_by_id("content").click()
        wd.find_element_by_name("group_name").send_keys(settings_ancillary.name)
        wd.find_element_by_name("group_header").send_keys(settings_ancillary.header)
        wd.find_element_by_name("group_footer").send_keys(settings_ancillary.footer)

    def submit_group_creation(self):
        wd = self.wd
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def destroy(self):
        self.wd.quit()
