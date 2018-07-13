
class HelperBase:

    def __init__(self, app):
        self.app = app


    def type(self, locator, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(locator).click()
            wd.find_element_by_name(locator).clear()
            wd.find_element_by_name(locator).send_keys(text)



    def is_valid(self):
        wd = self.app.wd
        try:
            wd.current_url
            return True
        except:
            return False