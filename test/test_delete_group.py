def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.go_to_group_page()
    app.group.select_first()
    app.group.delete()
    app.session.logout()
