import pytest
from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login( username="admin", password="secret")
    app.group.init_creation()
    app.group.fill_creation(Group(name="test", header="test", footer="test"))
    app.group.submit_creation()
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.init_creation()
    app.group.fill_creation(Group(name="", header="", footer=""))
    app.group.submit_creation()
    app.session.logout()

