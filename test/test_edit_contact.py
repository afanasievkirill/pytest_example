# -*- coding: utf-8 -*-
import mimesis

from model.contact import Contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
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
        bday_day="8",
        bday_month="July",
        bday_year="1991",
        aday="13",
        amonth="July",
        ayear="2011",
        address_2=mimesis.Address().address(),
        home=mimesis.Address().address(),
        notes=mimesis.Text().text(),
    )
    app.contact.edit_first(contact)
    app.session.logout()
