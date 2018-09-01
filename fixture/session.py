class SessionHelper:

    def __init__(self, app):
        self.app = app

    def group_page_settings(self):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_element_by_css_selector("body").click()

    def edit_page_settings(self):
        wd = self.app.wd
        self.app.navigation.open_home_page_edit()

    def login(self, username="admin", password ="secret"):
        wd = self.app.wd
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()


