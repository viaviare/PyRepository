from model.group import Group
import random

def test_modify_group_name(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="temp"))

    modify_data = Group(name="New Name")
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group.name = modify_data.name
    app.group.modify_by_id(group, modify_data)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)





    # def test_modify_group_header(app):
    #     if app.group.count == 0:
    #         app.group.create(Group(name="temp"))
    #
    #     old_groups = app.group.get_group_list()
    #     app.group.modify(Group (header="New Header"))
    #     new_groups = app.group.get_group_list()
    #     assert len(old_groups)  == len(new_groups)
