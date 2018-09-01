def test_del_contact_in_book_address(app2):
    app2.session.edit_page_settings()
    app2.session.login(username="admin", password="secret")
    app2.contact.del_contact_in_book_address()
    app2.session.logout()