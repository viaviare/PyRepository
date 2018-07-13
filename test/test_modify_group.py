from model.group import Group


def test_modify_group_name(app):
    if app.group.count == 0:
        app.group.create(Group(name="temp"))

    index = 0
    group = Group(name="New Name")
    old_groups = app.group.get_group_list()
    group.id = old_groups[index].id
    app.group.modify(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


    # def test_modify_group_header(app):
    #     if app.group.count == 0:
    #         app.group.create(Group(name="temp"))
    #
    #     old_groups = app.group.get_group_list()
    #     app.group.modify(Group (header="New Header"))
    #     new_groups = app.group.get_group_list()
    #     assert len(old_groups)  == len(new_groups)
