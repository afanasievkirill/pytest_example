# -*- coding: utf-8 -*-


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        contact = app.contact.get_data()
        app.contact.create(contact)
    app.contact.delete()
