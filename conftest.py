import pytest
from fixture.application import Application_test_add_group
from fixture.application import Application_test_add_contact_in_book_address

@pytest.fixture(scope = "session")
def app1(request):
    fixture = Application_test_add_group()
    request.addfinalizer(fixture.destroy)
    return fixture

@pytest.fixture(scope = "session")
def app(request):
    fixture = Application_test_add_contact_in_book_address()
    request.addfinalizer(fixture.destroy)
    return fixture