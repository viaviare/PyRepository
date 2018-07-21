from model.group import Group
import random



def test_delete_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="temp"))

    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_by_id(group.id)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups