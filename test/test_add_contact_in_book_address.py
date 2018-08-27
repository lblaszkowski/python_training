# -*- coding: utf-8 -*-
from model.contact import *


def test_add_contact_in_book_address(app):
    app.session.edit_page_settings()
    app.session.login(username="admin", password="secret")
    app.manager.user_data(Contact(firstname="Lukasz", middlename="Ebi", lastname="Blaszkowski",nickname="lblaszkowski"))
    app.manager.user_picture(Contact(title_photo="Chomik"))
    app.manager.companys_data(Contact(company="brak nazwy", address="Gdansk", home="Polska",
                                                     mobile="123456789",work="tester", fax="123456789"))
    app.manager.e_mail_data(Contact(email="janekkolasa@wp.pl", email2="janekkolasa2@wp.pl", email3="janekkolasa3@wp.pl"))
    app.manager.additional_data(Contact(homepage="brak",bday="2", bmonth="October",byear="1990",
                                aday="3",amonth="February",ayear="2001",address2="brak", phone2="brak", notes="brak"))
    app.manager.return_to_groups_page()
    app.session.logout()

