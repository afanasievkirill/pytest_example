# -*- coding: utf-8 -*-
from pytest import mark

from model.contact import Contact
from utils.data_generator import DataGenerator

data = DataGenerator()

ddt = [data.get_random_data() for i in range(2)]


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
