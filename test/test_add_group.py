# -*- coding: utf-8 -*-
from model.group import Group


    
def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.fill_firm(Group(name="dfsdf", header="vbnvbn", footer="qqqwewe"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.fill_firm(Group(name="", header="", footer=""))
    app.session.logout()

