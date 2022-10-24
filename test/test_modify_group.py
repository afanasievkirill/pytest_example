from model.group import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="name", header="header", footer="footer"))
    app.group.edit(Group(name="edit_name", header="edit_header", footer="edit_footer"))


def test_modify_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="name", header="header", footer="footer"))
    app.group.edit(Group(header="edit_header"))