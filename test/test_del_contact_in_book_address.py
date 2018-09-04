def test_del_contact_in_book_address(app):
    app.session.edit_page_settings()
    app.session.login(username="admin", password="secret")
    app.contact.del_contact_in_book_address()
    app.session.logout()