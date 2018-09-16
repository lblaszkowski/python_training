from model.group import Group


def test_add_group(app):
    app.session.group_page_settings()
    app.group.creation(Group(name="test", header="test", footer="test"))


def test_add_empty_group(app):
    app.session.group_page_settings()
    app.group.creation( Group(name="", header="", footer=""))


