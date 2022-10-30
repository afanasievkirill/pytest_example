from model.group import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="name", header="header", footer="footer"))
    old_groups = app.group.get_group_list()
    app.group.edit(Group(name="edit_name", header="edit_header", footer="edit_footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="name", header="header", footer="footer"))
    old_groups = app.group.get_group_list()
    app.group.edit(Group(header="edit_header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
