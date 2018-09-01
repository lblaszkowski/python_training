from model.group import *


def test_add_group(app1):
    app1.session.group_page_settings()
    app1.session.login( username="admin", password="secret")
    app1.group.creation(Group(name="test", header="test", footer="test"))
    app1.session.logout()

def test_add_empty_group(app1):
    app1.session.group_page_settings()
    app1.session.login(username="admin", password="secret")
    app1.group.creation( Group(name="", header="", footer=""))
    app1.session.logout()

