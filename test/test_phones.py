def test_phones_on_home_page(app):
    if app.contact.count() == 0:
        contact = app.contact.get_data()
        app.contact.create(contact)
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)

    assert contact_from_home_page.home_phone == app.contact.clear_phone(
        contact_from_edit_page.home_phone
    )
    assert contact_from_home_page.mobile_phone == app.contact.clear_phone(
        contact_from_edit_page.mobile_phone
    )
    assert contact_from_home_page.work_phone == app.contact.clear_phone(
        contact_from_edit_page.work_phone
    )
    assert contact_from_home_page.home_phone_2 == app.contact.clear_phone(
        contact_from_edit_page.home_phone_2
    )


def test_phones_on_view_page(app):
    if app.contact.count() == 0:
        contact = app.contact.get_data()
        app.contact.create(contact)
    contact_from_view_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)

    assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
    assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
    assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
    assert contact_from_view_page.home_phone_2 == contact_from_edit_page.home_phone_2
