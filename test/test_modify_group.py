from model.group import Group


def test_modify_first_group(app):
    app.group.edit(Group(name="edit_name", header="edit_header", footer="edit_footer"))


def test_modify_header(app):
    app.group.edit(Group(header="edit_header"))
