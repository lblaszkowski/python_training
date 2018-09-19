from model.contact import Contact

def test_del_contact_in_book_address(app):
    app.session.edit_page_settings()
    if app.group.count() == 0:
        app.contact.del_contact_in_book_address()
