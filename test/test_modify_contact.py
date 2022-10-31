# -*- coding: utf-8 -*-
from random import randrange

from model.contact import Contact


def test_modify_contact(app):
    modify_contact = app.contact.get_data()
    if app.contact.count() == 0:
        create_contact = app.contact.get_data()
        app.contact.create(create_contact)
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))

    modify_contact.id = old_contact[index].id
    app.contact.edit_by_index(modify_contact, index)

    assert len(old_contact) == app.contact.count()

    new_contact = app.contact.get_contact_list()
    old_contact[index] = modify_contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(
        new_contact, key=Contact.id_or_max
    )
