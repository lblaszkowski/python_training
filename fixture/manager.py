class ContactHelper:

    def __init__(self, app):
        self.app = app


    def user_data(self, auxiliary_contact_settings):
        wd = self.app.wd
        wd.find_element_by_name("firstname").send_keys(auxiliary_contact_settings.firstname)
        wd.find_element_by_name("middlename").send_keys(auxiliary_contact_settings.middlename)
        wd.find_element_by_name("lastname").send_keys(auxiliary_contact_settings.lastname)
        wd.find_element_by_name("nickname").send_keys(auxiliary_contact_settings.nickname)

    def user_picture(self,auxiliary_contact_settings):
        wd = self.app.wd
        wd.find_element_by_name("photo").send_keys("C:\\python_training\\image\\images.jpg")
        wd.find_element_by_name("title").send_keys(auxiliary_contact_settings.title_photo)

    def companys_data(self, company_data_settings):
        wd = self.app.wd
        wd.find_element_by_name("company").send_keys(company_data_settings.company)
        wd.find_element_by_name("address").send_keys(company_data_settings.address)
        wd.find_element_by_name("home").send_keys(company_data_settings.home)
        wd.find_element_by_name("mobile").send_keys(company_data_settings.mobile)
        wd.find_element_by_name("work").send_keys(company_data_settings.work)
        wd.find_element_by_name("fax").send_keys(company_data_settings.fax)

    def e_mail_data(self, auxiliary_contact_settings):
        wd = self.app.wd
        wd.find_element_by_name("email").send_keys(auxiliary_contact_settings.email)
        wd.find_element_by_name("email2").send_keys(auxiliary_contact_settings.email2)
        wd.find_element_by_name("email3").send_keys(auxiliary_contact_settings.email3)

    def additional_data(self, additional_data_settings):
        wd = self.app.wd
        wd.find_element_by_name("homepage").send_keys(additional_data_settings.homepage)
        wd.find_element_by_name("bday").send_keys(additional_data_settings.bday)
        wd.find_element_by_name("bmonth").send_keys(additional_data_settings.bmonth)
        wd.find_element_by_name("byear").send_keys(additional_data_settings.byear)
        wd.find_element_by_name("aday").send_keys(additional_data_settings.aday)
        wd.find_element_by_name("amonth").send_keys(additional_data_settings.amonth)
        wd.find_element_by_name("ayear").send_keys(additional_data_settings.ayear)
        wd.find_element_by_name("address2").send_keys(additional_data_settings.address2)
        wd.find_element_by_name("phone2").send_keys(additional_data_settings.phone2)
        wd.find_element_by_name("notes").send_keys(additional_data_settings.notes)
        wd.find_element_by_name("submit").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()