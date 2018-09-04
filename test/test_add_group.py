from model.group import *


def test_add_group(app):
    app.session.group_page_settings()
    app.session.login( username="admin", password="secret")
    app.group.creation(Group(name="test", header="test", footer="test"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.group_page_settings()
    app.session.login(username="admin", password="secret")
    app.group.creation( Group(name="", header="", footer=""))
    app.session.logout()

