# -*- coding: utf-8 -*-
from model.group import Group


    
def test_add_group(app):
    app.group.create(Group(name="dfsdf", header="vbnvbn", footer="qqqwewe"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

