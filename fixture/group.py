class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def init_creation(self):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()

    def fill_creation(self, settings_ancillary):
        wd = self.app.wd
        wd.find_element_by_id("content").click()
        wd.find_element_by_name("group_name").send_keys(settings_ancillary.name)
        wd.find_element_by_name("group_header").send_keys(settings_ancillary.header)
        wd.find_element_by_name("group_footer").send_keys(settings_ancillary.footer)

    def submit_creation(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

