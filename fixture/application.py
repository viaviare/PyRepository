from selenium import webdriver

from fixture.helper import HelperBase
from fixture.navigation import NavigationHelper
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(2)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.helper = HelperBase(self)
        self.navigator = NavigationHelper(self)


    def destroy(self):
        self.wd.quit()