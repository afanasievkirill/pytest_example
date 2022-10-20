from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.go_to_group_page()
    app.group.select_first()
    app.group.edit(Group(name="edit_name", header="edit_header", footer="edit_footer"))
    app.session.logout()
