from model.group import Group


def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="temp"))

    index=0
    old_groups = app.group.get_group_list()
    app.group.delete(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups == new_groups

