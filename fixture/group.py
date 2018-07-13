



class GroupHelper:

    def __init__(self, app):
        self.app = app


    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()


    def fill_group_form(self, group):
        wd = self.app.wd
        wd.find_element_by_id("content").click()
        self.app.helper.type("group_name", group.name)
        self.app.helper.type("group_header", group.header)
        self.app.helper.type("group_footer", group.footer)



    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()


    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()


    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()


    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()


    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()