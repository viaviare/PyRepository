# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(request)
    return fixture

    
def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.fill_firm(Group(name="dfsdf", header="vbnvbn", footer="qqqwewe"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.fill_firm(Group(name="", header="", footer=""))
    app.session.logout()

