# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    modify_contact = app.contact.get_data()
    if app.contact.count() == 0:
        create_contact = app.contact.get_data()
        app.contact.create(create_contact)
    old_contact = app.contact.get_contact_list()
    modify_contact.id = old_contact[0].id
    app.contact.edit_first(modify_contact)

    assert len(old_contact) == app.contact.count()

    new_contact = app.contact.get_contact_list()
    old_contact[0] = modify_contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(
        new_contact, key=Contact.id_or_max
    )
