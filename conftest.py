import pytest
from fixture.application import Application


fixture = None

@pytest.fixture
def app():
    if fixture is None:
        login()
    else:
        if not fixture.is_valid:
            login()
    return fixture


def login():
    global fixture
    fixture = Application()
    fixture.session.login(username="admin", password="secret")


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)