from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)


    def open_home_page(self):
        wd = self.wd
        # open home page
        wd.get("http://localhost/addressbook/group.php")


    def destroy(self):
        self.wd.quit()