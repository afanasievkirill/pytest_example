# -*- coding: utf-8 -*-
from random import randrange


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        contact = app.contact.get_data()
        app.contact.create(contact)
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    app.contact.delete(index)

    assert len(old_contact) - 1 == app.contact.count()

    new_contact = app.contact.get_contact_list()
    old_contact[index : index + 1] = []
    assert old_contact == new_contact
