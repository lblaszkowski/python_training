from model.group import *


def test_modify_group_name(app):
    app.session.group_page_settings()
    app.group.modify_first_group(Group(name="New group"))


def test_modify_group_header(app):
    app.session.group_page_settings()
    app.group.modify_first_group(Group(header="New header"))











