


class SessionHelper:


    def __init__(self, app):
        self.app = app


    def login(self, username, password):
        wd = self.app.wd
        if self.check_logged_in():
            if self.logged_in(username):
                return
            else:
                self.logout()
        self.app.navigator.open_start_page()
        self.app.helper.type("user", username)
        self.app.helper.type("pass", password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()


    def logout(self):
        wd = self.app.wd
        if self.check_logged_in():
            wd.find_element_by_link_text("Logout").click()


    def check_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout"))>0


    def logged_in(self, username):
        wd = self.app.wd
        if self.check_logged_in() and wd.find_element_by_css_selector("form[name='logout'] b").text == "(" + username + ")":
            return True