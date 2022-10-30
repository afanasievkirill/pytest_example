# -*- coding: utf-8 -*-


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        contact = app.contact.get_data()
        app.contact.create(contact)
    old_contact = app.contact.get_contact_list()
    app.contact.delete()
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) - 1 == len(new_contact)
