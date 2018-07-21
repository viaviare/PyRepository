from model.group import Group

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        self.app.navigator.open_groups_page()
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def modify(self, index, new_group_data):
        wd = self.app.wd
        self.app.navigator.open_groups_page()
        self.select_group(index)
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def modify_by_id(self, group, modify_data):
        wd = self.app.wd
        self.app.navigator.open_groups_page()
        self.select_group_by_id(group.id)
        wd.find_element_by_name("edit").click()
        self.fill_group_form(modify_data)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None


    def delete(self, index):
        wd = self.app.wd
        self.app.navigator.open_groups_page()
        self.select_group(index)
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None


    def delete_by_id(self, id):
        wd = self.app.wd
        self.app.navigator.open_groups_page()
        self.select_group_by_id(id)
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None


    def fill_group_form(self, group):
        wd = self.app.wd
        wd.find_element_by_id("content").click()
        self.app.helper.type("group_name", group.name)
        self.app.helper.type("group_header", group.header)
        self.app.helper.type("group_footer", group.footer)


    def select_group(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()


    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def count(self):
        wd = self.app.wd
        self.app.navigator.open_groups_page()
        return len(wd.find_elements_by_css_selector("span.group"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.app.navigator.open_groups_page()
            self.group_cache=[]
            elements = wd.find_elements_by_css_selector("span.group")
            for item in elements:
                name = item.text
                id = item.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=name, id=int(id)))
        return list(self.group_cache)