import pytest
import json
from fixture.application import Application


fixture = None
target = None

@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    with open (request.config.getoption("--target")) as config_file:
        target = json.load(config_file)
    if fixture is None or not fixture.helper.is_valid:
        fixture = Application(browser=browser, baseUrl=target['baseUrl'])
    fixture.session.login(username=target['username'], password=target['password'])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")