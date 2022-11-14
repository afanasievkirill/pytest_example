# -*- coding: utf-8 -*-
from pytest import mark

from model.contact import Contact
from data.contacts import ddt


@mark.parametrize("contact", ddt, ids=[repr(x) for x in ddt])
def test_add_contact(app, contact):
    old_contact = app.contact.get_contact_list()
    app.contact.create(contact)

    assert len(old_contact) + 1 == app.contact.count()

    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(
        new_contact, key=Contact.id_or_max
    )


def test_add_contact_from_data(app, data_contacts):
    contact = data_contacts
    old_contact = app.contact.get_contact_list()
    app.contact.create(contact)

    assert len(old_contact) + 1 == app.contact.count()

    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(
        new_contact, key=Contact.id_or_max
    )


def test_add_contact_from_json(app, json_contacts):
    contact = json_contacts
    old_contact = app.contact.get_contact_list()
    app.contact.create(contact)

    assert len(old_contact) + 1 == app.contact.count()

    new_contact = app.contact.get_contact_list()
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(
        new_contact, key=Contact.id_or_max
    )
