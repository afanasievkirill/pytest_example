from random import randrange

from model.group import Group


def test_modify_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="name", header="header", footer="footer"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="edit_name", header="edit_header", footer="edit_footer")
    group.id = old_groups[index].id

    app.group.edit(group, index)

    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(
        new_groups, key=Group.id_or_max
    )
