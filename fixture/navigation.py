class NavigationHelper:
    def __init__(self, app):
        self.app = app

    def open_start_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook")

    def open_main_page(self):
        wd = self.app.wd
        if wd.current_url == "http://localhost/addressbook" and len(wd.find_elements_by_link_text("Logout")) > 0:
            return
        wd.find_element_by_link_text("home").click()

    def open_groups_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("edit")) > 0:
            wd.find_element_by_link_text("groups").click()
