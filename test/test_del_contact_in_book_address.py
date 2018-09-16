from model.contact import Contact

def test_del_contact_in_book_address(app):
    app.session.edit_page_settings()
    if app.group.count_checkbox() == 0:
        app.group.fill_all_user_data(Contact(firstname="Test"))
    app.contact.del_contact_in_book_address()
