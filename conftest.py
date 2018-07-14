import pytest
from fixture.application import Application


fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None or not fixture.helper.is_valid:
        browser = request.config.getoption("--browser")
        baseUrl = request.config.getoption("--baseUrl")
        fixture = Application(browser=browser, baseUrl=baseUrl)
    fixture.session.login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook")