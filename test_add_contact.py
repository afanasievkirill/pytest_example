# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest


from contact import Contact


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_home_page(self, wd: webdriver):
        wd.get("http://localhost/addressbook/group.php")

    def goto_home_page(self, wd: webdriver):
        wd.find_element_by_link_text("home").click()

    def login(self, wd: webdriver, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def create_contact(self, wd: webdriver, contact: Contact):
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_xpath("//input[@type='file']").send_keys(contact.photo_path)
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        wd.find_element_by_name("work").send_keys(contact.work_phone)
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").send_keys(contact.email_2)
        wd.find_element_by_name("email3").send_keys(contact.email_3)
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday_day)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(
            contact.bday_month
        )
        wd.find_element_by_name("byear").send_keys(contact.bday_year)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
        wd.find_element_by_name("ayear").send_keys(contact.ayear)
        wd.find_element_by_name("address2").send_keys(contact.address_2)
        wd.find_element_by_name("phone2").send_keys(contact.home)
        wd.find_element_by_name("notes").send_keys(contact.notes)

        wd.find_element_by_xpath("(//input[@value='Enter'][2])").click()

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        contact = Contact(
            firstname="firstname",
            lastname="lastname",
            middlename="middlename",
            nickname="nickname",
            photo_path=".\\README.md",
            title="test_company",
            company="company_name",
            address="adress_1",
            home_phone="+795-333-33-33",
            mobile_phone="+7(495)-33-33-33",
            work_phone="+7(495)-333-33-33",
            fax="+7(495)-33-33-33",
            email="test@test.com",
            email_2="test@test.com",
            email_3="test@test.com",
            homepage="https://google.com",
            bday_day="7",
            bday_month="June",
            bday_year="1990",
            aday="12",
            amonth="July",
            ayear="2010",
            address_2="address_2",
            home="home_2",
            notes="notes",
        )
        self.create_contact(wd, contact)
        self.goto_home_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
