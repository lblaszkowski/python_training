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
        self.app.navigation.open_home_page()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
        wd.close()

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, usernamey):
        wd = self.app.wd
        return len(wd.find_element_by_xpath("//div/div/[1]/from/b")).text == "("+usernamey+")"


    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)





