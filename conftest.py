import pytest
from fixture.application import *


@pytest.fixture(scope = "session")
def app1(request):
    fixture = Application_test_add_group()
    request.addfinalizer(fixture.destroy)
    return fixture

@pytest.fixture(scope = "session")
def app2(request):
    fixture = Application_test_add_contact_in_book_address()
    request.addfinalizer(fixture.destroy)
    return fixture