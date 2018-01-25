# -*- coding: utf-8 -*-
from selenium import webdriver
from group import Group
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(60)
    
    def test_add_group(self):
        success = True
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_groups_page(wd)
        self.fill_group_firm(wd, Group(name="dfsdf", header="vbnvbn", footer="qqqwewe"))
        self.return_to_groups_page(wd)
        self.logout(wd)

    def test_add_empty_group(self):
        success = True
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_groups_page(wd)
        self.fill_group_firm(wd, Group(name="", header="", footer=""))
        self.return_to_groups_page(wd)
        self.logout(wd)


    def fill_group_firm(self, wd, group):
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group firm
        wd.find_element_by_id("content").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()




    def open_groups_page(self, wd):
        # open groups page
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, username, password):
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self, wd):
        # open home page
        wd.get("http://localhost/addressbook/group.php")

    def tearDown(self):
        self.wd.quit()

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self, wd):
        # return to groups page
        wd.find_element_by_link_text("group page").click()

if __name__ == '__main__':
    unittest.main()
