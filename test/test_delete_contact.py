# -*- coding: utf-8 -*-


def test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.go_to_contact_page()
    app.contact.select_first()
    app.contact.delete()
    app.contact.go_to_contact_page()
    app.session.logout()
