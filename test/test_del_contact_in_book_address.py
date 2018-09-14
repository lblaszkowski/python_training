def test_del_contact_in_book_address(app):
    app.session.edit_page_settings()
    app.contact.del_contact_in_book_address()
