# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    modify_contact = app.contact.get_data()
    print(app.contact.count())
    if app.contact.count() == 0:
        create_contact = app.contact.get_data()
        app.contact.create(create_contact)
    app.contact.edit_first(modify_contact)
