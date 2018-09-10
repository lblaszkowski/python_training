import pytest
from fixture.application import *

@pytest.fixture(scope = "session")
def app(request):
    fixture = Application()
    fixture.session.login( username="admin", password="secret")
    def fin():
        fixture.session.logout()
        fixture.destroy
    request.addfinalizer(fin)
    return fixture


# @pytest.fixture(scope = "session")
# def app(request):
#     fixture = Application()
#     request.addfinalizer(fixture.destroy)
#     return fixture