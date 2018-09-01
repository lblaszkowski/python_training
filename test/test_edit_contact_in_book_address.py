from model.contact import Contact

def test_edit_contact_in_book_address(app2):
    app2.session.edit_page_settings()
    app2.session.login(username="admin", password="secret")
    app2.contact.edit_contact_in_book_address(
        Contact(firstname="Justyna", middlename="", lastname="Nowik", nickname="JNowik",
                title_photo="zwierzęta", company="", address="Warszawa", home="Polska", mobile="99999999999",
                work="model", fax="9876678909", email="JNowik@o2.pl", email2="JNowik@onet.pl",
                email3="", homepage="", bday="5", bmonth="February", byear="2001",
                aday="26", amonth="October", ayear="2014", address2="", phone2="", notes="")
        )
    app2.contact.return_to_groups_page()
    app2.session.logout()