from random import randrange
from model.contact import Contact


def test_contact_info_on_home_page(app):
    if app.contact.count() == 0:
        contact = app.contact.get_data()
        app.contact.create(contact)

    contact: list[Contact] = app.contact.get_contact_list()
    index: int = randrange(len(contact))

    contact_from_home_page: Contact = app.contact.get_contact_list()[index]
    contact_from_edit_page: Contact = app.contact.get_contact_info_from_edit_page(index)

    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address

    assert (
        contact_from_home_page.all_emails_from_home_page
        == app.contact.merge_all_emails_like_home_page(contact_from_edit_page)
    )

    assert (
        contact_from_home_page.all_phones_from_home_page
        == app.contact.merge_all_phones_like_home_page(contact_from_edit_page)
    )
