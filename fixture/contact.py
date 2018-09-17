class ContactHelper:

    def __init__(self, app):
        self.app = app


    def fill_all_user_data(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").send_keys(contact .nickname)
        wd.find_element_by_name("photo").send_keys("C:\\python_training\\image\\images.jpg")
        wd.find_element_by_name("title").send_keys(contact.title_photo)
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").send_keys(contact.work)
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        wd.find_element_by_name("bday").send_keys(contact.bday)
        wd.find_element_by_name("bmonth").send_keys(contact.bmonth)
        wd.find_element_by_name("byear").send_keys(contact.byear)
        wd.find_element_by_name("aday").send_keys(contact.aday)
        wd.find_element_by_name("amonth").send_keys(contact.amonth)
        wd.find_element_by_name("ayear").send_keys(contact.ayear)
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").send_keys(contact.notes)
        wd.find_element_by_name("submit").click()

    def del_contact_in_book_address(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_name('selected[]').click()
        wd.find_element_by_xpath('//*[@id="content"]/form[2]/div[2]/input').click()
        wd.switch_to_alert().accept()

    def edit_contact_in_book_address(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_name('selected[]').click()
        wd.find_element_by_xpath('//*[@id="maintable"]/tbody/tr[3]/td[8]/a').click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("photo").send_keys("C:\\python_training\\image\\images1.jpg")
        wd.find_element_by_name("title").send_keys(contact.title_photo)
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").send_keys(contact.work)
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("bday").send_keys(contact.bday)
        wd.find_element_by_name("bmonth").send_keys(contact.bmonth)
        wd.find_element_by_name("byear").send_keys(contact.byear)
        wd.find_element_by_name("aday").send_keys(contact.aday)
        wd.find_element_by_name("amonth").send_keys(contact.amonth)
        wd.find_element_by_name("ayear").send_keys(contact.ayear)
        wd.find_element_by_name("update").click()


    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.fill_all_user_data()
        return len(wd.find_elements_by_name("selected[]"))

