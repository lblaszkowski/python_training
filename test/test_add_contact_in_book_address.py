# -*- coding: utf-8 -*-
import pytest
from fixture.fikstury_application import Fikstury_application
from model.settings_ancillary import *


@pytest.fixture
def app(request):
    fixture = Fikstury_application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact_in_book_address(app):
    app.session.login( username="admin", password="secret")
    app.user_data(User_basic_data(firstname="Lukasz", middlename="Ebi", lastname="Blaszkowski", nickname="lblaszkowski"))
    app.adding_a_picture_and_name( User_picture(title_photo="Chomik"))
    app.companys_data(Company_data_settings(company="brak nazwy", address="Gdansk", home="Polska",
                                                     mobile="123456789",work="tester", fax="123456789"))
    app.e_mail_data( Data_email(email="janekkolasa@wp.pl", email2="janekkolasa2@wp.pl", email3="janekkolasa3@wp.pl"))
    app.additional_data( Additional_data_settings(homepage="brak",bday="2", bmonth="October",byear="1990",
                                aday="3",amonth="February",ayear="2001",address2="brak", phone2="brak", notes="brak"))
    app.return_to_groups_page()
    app.session.logout()

