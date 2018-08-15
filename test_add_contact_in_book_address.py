# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from selenium.webdriver.support.select import Select
from auxiliary_contact_settings import *



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

    def user_data(self, wd, auxiliary_contact_settings):
        wd.find_element_by_name("firstname").send_keys(auxiliary_contact_settings.firstname)
        wd.find_element_by_name("middlename").send_keys(auxiliary_contact_settings.middlename)
        wd.find_element_by_name("lastname").send_keys(auxiliary_contact_settings.lastname)
        wd.find_element_by_name("nickname").send_keys(auxiliary_contact_settings.nickname)

    def adding_a_picture_and_name(self, wd, auxiliary_contact_settings):
        wd.find_element_by_name("photo").send_keys("C:\\python_training\\image\\images.jpg")
        wd.find_element_by_name("title").send_keys(auxiliary_contact_settings.title_photo)

    def companys_data(self, wd, company_data_settings):
        wd.find_element_by_name("company").send_keys(company_data_settings.company)
        wd.find_element_by_name("address").send_keys(company_data_settings.address)
        wd.find_element_by_name("home").send_keys(company_data_settings.home)
        wd.find_element_by_name("mobile").send_keys(company_data_settings.mobile)
        wd.find_element_by_name("work").send_keys(company_data_settings.work)
        wd.find_element_by_name("fax").send_keys(company_data_settings.fax)

    def e_mail_data(self, wd, auxiliary_contact_settings):
        wd.find_element_by_name("email").send_keys(auxiliary_contact_settings.email)
        wd.find_element_by_name("email2").send_keys(auxiliary_contact_settings.email2)
        wd.find_element_by_name("email3").send_keys(auxiliary_contact_settings.email3)

    def additional_data(self, wd, additional_data_settings):
        wd.find_element_by_name("homepage").send_keys(additional_data_settings.homepage)
        Select(wd.find_element_by_name("bday")).select_by_visible_text(additional_data_settings.bday)
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(additional_data_settings.bmonth)
        wd.find_element_by_name("byear").send_keys(additional_data_settings.byear)
        Select(wd.find_element_by_name("aday")).select_by_visible_text(additional_data_settings.aday)
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(additional_data_settings.amonth)
        wd.find_element_by_name("ayear").send_keys(additional_data_settings.ayear)
        wd.find_element_by_name("address2").send_keys(additional_data_settings.address2)
        wd.find_element_by_name("phone2").send_keys(additional_data_settings.phone2)
        wd.find_element_by_name("notes").send_keys(additional_data_settings.notes)

    def return_to_groups_page(self, wd):
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_add_contact_in_book_address(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.user_data(wd, User_basic_data(firstname="Lukasz", middlename="Ebi", lastname="Blaszkowski", nickname="lblaszkowski"))
        self.adding_a_picture_and_name(wd, User_picture(title_photo="Chomik"))
        self.companys_data(wd, Company_data_settings(company="brak nazwy", address="Gdansk", home="Polska",
                                                     mobile="123456789",work="tester", fax="123456789"))
        self.e_mail_data(wd, Data_email(email="janekkolasa@wp.pl", email2="janekkolasa2@wp.pl", email3="janekkolasa3@wp.pl"))
        self.additional_data(wd, Additional_data_settings(homepage="brak",bday="2", bmonth="October",byear="1990",
                                aday="3",amonth="February",ayear="2001",address2="brak", phone2="brak", notes="brak"))
        self.return_to_groups_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()




if __name__ == '__main__':
    unittest.main()
