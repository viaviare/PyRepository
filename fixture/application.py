from selenium import webdriver

from fixture.helper import HelperBase
from fixture.navigation import NavigationHelper
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self, browser, baseUrl):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(0)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.helper = HelperBase(self)
        self.navigator = NavigationHelper(self)
        self.baseUrl = baseUrl


    def destroy(self):
        self.wd.quit()