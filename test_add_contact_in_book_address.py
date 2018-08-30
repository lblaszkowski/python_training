# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from selenium.webdriver.support.select import Select
from contact import Contact



def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_contact_in_book_address(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/edit.php")

    def login(self, wd, username="admin", password="secret"):
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def fill_all_user_data(self, wd, contact):
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
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
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element_by_name("byear").send_keys(contact.byear)
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        wd.find_element_by_name("ayear").send_keys(contact.ayear)
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").send_keys(contact.notes)

    def return_to_groups_page(self, wd):
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_add_contact_in_book_address(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.fill_all_user_data(wd, Contact(firstname="Lukasz", middlename="Ebi", lastname="Blaszkowski", nickname="lblaszkowski",
                                        title_photo="Chomik",company="brak nazwy", address="Gdansk", home="Polska",
                                        mobile="123456789",work="tester", fax="123456789",email="janekkolasa@wp.pl",
                                        email2="janekkolasa2@wp.pl", email3="janekkolasa3@wp.pl",homepage="brak",
                                        bday="2", bmonth="October", byear="1990",aday="3", amonth="February",
                                        ayear="2001", address2="brak", phone2="brak", notes="brak"))
        self.return_to_groups_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()




if __name__ == '__main__':
    unittest.main()
