# -*- coding: utf-8 -*-
from model.group import Group



def test_add_group(app, db, json_groups, check_ui):  #data_groups, json_groups are the fixtures
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

    if check_ui:
        new_groups = map(lambda gr: Group(id=gr.id, name=gr.name.strip()), db.get_group_list())  # spaces at the end of name
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)




