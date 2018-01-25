# -*- coding: utf-8 -*-
from group import Group
from application import Application
import pytest



@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(request)
    return fixture

    
def test_add_group(app):
    app.login(username="admin", password="secret")
    app.fill_group_firm(Group(name="dfsdf", header="vbnvbn", footer="qqqwewe"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.fill_group_firm(Group(name="", header="", footer=""))
    app.logout()

