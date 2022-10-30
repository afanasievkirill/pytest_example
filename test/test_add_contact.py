# -*- coding: utf-8 -*-
import mimesis

from model.contact import Contact


def test_add_contact(app):
    contact = Contact(
        firstname=mimesis.Person().first_name(),
        lastname=mimesis.Person().last_name(),
        middlename=mimesis.Person().full_name(),
        nickname=mimesis.Food().fruit(),
        photo_path="/README.md",
        title=mimesis.Text().title(),
        company=mimesis.Text().title(),
        address=mimesis.Address().address(),
        home_phone=mimesis.Person().telephone(),
        mobile_phone=mimesis.Person().telephone(),
        work_phone=mimesis.Person().telephone(),
        fax=mimesis.Person().telephone(),
        email=mimesis.Person().email(),
        email_2=mimesis.Person().email(),
        email_3=mimesis.Person().email(),
        homepage=mimesis.Internet().url(),
        bday_day="7",
        bday_month="June",
        bday_year="1990",
        aday="12",
        amonth="July",
        ayear="2010",
        address_2=mimesis.Address().address(),
        home=mimesis.Address().address(),
        notes=mimesis.Text().text(),
    )
    old_contact = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)
