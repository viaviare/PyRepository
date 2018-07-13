

class NavigationHelper:


    def __init__(self, app):
        self.app = app


    def open_start_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")


