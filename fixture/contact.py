from model.contact import Contact
import mimesis
import re
from selenium.webdriver.support.ui import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def go_to_contact_page(self) -> None:
        """_summary_"""
        wd = self.app.wd
        if not (
            wd.current_url.endswith("/group.php")
            and len(wd.find_elements_by_xpath("//input[@value='Delete']")) > 0
        ):
            wd.find_element_by_link_text("home").click()

    def create(self, contact: Contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.__fill_conctact_form(contact)
        wd.find_element_by_xpath("(//input[@value='Enter'][2])").click()
        wd.find_element_by_link_text("home").click()
        self.contact_cache = None

    def select_first(self):
        self.select_by_index(0)

    def select_by_index(self, index: int):
        wd = self.app.wd
        wd.find_elements_by_xpath("//tr//td/input[@type='checkbox']")[index].click()

    def count(self):
        wd = self.app.wd
        self.go_to_contact_page()
        return len(wd.find_elements_by_xpath("//tr//td/input[@type='checkbox']"))

    def edit_first(self, contact: Contact, index: int = 0):
        self.edit_by_index(contact, index)

    def edit_by_index(self, contact: Contact, index: int):
        """
            Метод редактирует Контакт по индексу с помощью формы.
        Args:
            contact (Contact): Объект Contact ./model/contact.py
            index (int): порядковый номер элемента в списке контактов
            на странице: /addressbook/index.php
        """
        wd = self.app.wd
        self.open_contact_by_index(index)
        self.__fill_conctact_form(contact)
        wd.find_element_by_xpath("(//input[@value='Update'][2])").click()
        wd.find_element_by_link_text("home").click()
        self.contact_cache = None

    def get_contact_info_from_edit_page(self, index: int):
        """
            Метод возвращает данные о Контакте с страницы:
            addressbook/edit.php?id=${index}
            по айди.
        Args:
            index (int): порядковый номер элемента в списке контактов
            на странице: /addressbook/index.php
        Returns:
            Contact : Объект Contact ./model/contact.py
        """
        wd = self.app.wd
        self.open_contact_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").text
        id = wd.find_element_by_name("id").get_attribute("value")

        home_phone = wd.find_element_by_name("home").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        home_phone_2 = wd.find_element_by_name("phone2").get_attribute("value")

        email = wd.find_element_by_name("email").get_attribute("value")
        email_2 = wd.find_element_by_name("email2").get_attribute("value")
        email_3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(
            firstname=firstname,
            lastname=lastname,
            id=id,
            address=address,
            home_phone=home_phone,
            mobile_phone=mobile_phone,
            work_phone=work_phone,
            home_phone_2=home_phone_2,
            email=email,
            email_2=email_2,
            email_3=email_3,
        )

    def open_contact_by_index(self, index: int):
        wd = self.app.wd
        self.go_to_contact_page()
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()

    def open_contact_view_by_index(self, index: int):
        wd = self.app.wd
        self.go_to_contact_page()
        wd.find_elements_by_xpath("//img[@title='Details']")[index].click()

    def delete(self, index: int):
        wd = self.app.wd
        self.go_to_contact_page()
        self.select_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.go_to_contact_page()
        self.contact_cache = None

    def __fill_conctact_form(self, contact: Contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_xpath("//input[@type='file']").send_keys(contact.photo_path)
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_phone)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email_2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email_3)
        wd.find_element_by_name("homepage").clear()
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
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address_2)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.home_phone_2)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)

    def get_random_data(self) -> Contact:
        """
            Функция создает объект с рандомными данными
            для использования в тестах с помощью библиотеки mimesis.
        Returns:
            Contact: Объект Contact ./model/contact.py
        """
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
            home_phone_2=mimesis.Person().telephone(),
            notes=mimesis.Text().text(),
        )
        return contact

    def get_data(self) -> Contact:
        contact = Contact(
            firstname="firstname",
            lastname="lastname",
            middlename="middlename",
            nickname="nickname",
            photo_path="/README.md",
            title="title",
            company="company",
            address="address",
            home_phone="9153003030",
            mobile_phone="9204004040",
            work_phone="9255005050",
            fax="9306006060",
            email="email@email.com",
            email_2="email@email.com",
            email_3="email@email.com",
            homepage="https://localhost",
            bday_day="7",
            bday_month="June",
            bday_year="1990",
            aday="12",
            amonth="July",
            ayear="2010",
            address_2=mimesis.Address().address(),
            home_phone_2="9357007070",
            notes="notes",
        )
        return contact

    contact_cache = None

    def get_contact_list(self):
        """
            Функция проверяет кэш, в случае его отсутсвия
            перебирает записи на странице:
            addressbook/index.php и возвращает их список.
        Returns:
            Contact[]: Лист объектов Contact ./model/contact.py
        """
        if self.contact_cache is None:
            wd = self.app.wd
            self.go_to_contact_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_css_selector("td input").get_attribute(
                    "value"
                )
                list_td = []
                list_td = element.find_elements_by_css_selector("td")
                firstname = list_td[2].text
                lastname = list_td[1].text
                address = list_td[3].text
                all_emails = list_td[4].text
                all_phones = list_td[5].text
                self.contact_cache.append(
                    Contact(
                        firstname=firstname,
                        lastname=lastname,
                        id=id,
                        address=address,
                        all_phones_from_home_page=all_phones,
                        all_emails_from_home_page=all_emails,
                    )
                )
        return list(self.contact_cache)

    def get_contact_from_view_page(self, index) -> Contact:
        """_summary_

        Args:
            index (_type_): _description_

        Returns:
            Contact: _description_
        """
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        home_phone_2 = re.search("P: (.*)", text).group(1)
        return Contact(
            home_phone=home_phone,
            mobile_phone=mobile_phone,
            work_phone=work_phone,
            home_phone_2=home_phone_2,
        )

    def clear_phone(self, phone: str) -> str:
        """
            Метод приводит телефоны с формы addressbook/edit.php
            к виду в списка формы addressbook/index.php

        Args:
            phone (str): строка вида +7(920)-200-20-20

        Returns:
            str: строка вида +79202002020
        """
        return re.sub("[() -.]", "", phone)

    def clear_email(self, email: str) -> str:
        """
            Метод приводит телефоны с формы addressbook/edit.php
            к виду в списка формы addressbook/index.php

        Args:
            phone (str): строка вида test@test.ru  /te st@test.ru

        Returns:
            str: строка вида test@test.ru
        """
        return re.sub(" ", "", email)

    def merge_all_phones_like_home_page(self, contact: Contact) -> str:
        """
            Метод возвращает строку телефонов в представлении списка
            с страницы: addressbook/index.php
        Args:
            contact (Contact): объект Contact ./model/contact.py

        Returns:
            str: строка all_phones_from_home_page
            объекта Contact ./model/contact.py
        """
        return "\n".join(
            filter(
                lambda x: x != "",
                map(
                    lambda x: self.clear_phone(x),
                    filter(
                        lambda x: x is not None,
                        [
                            contact.home_phone,
                            contact.mobile_phone,
                            contact.work_phone,
                            contact.home_phone_2,
                        ],
                    ),
                ),
            )
        )

    def merge_all_emails_like_home_page(self, contact: Contact) -> str:
        """
            Метод возвращает строку емейлов в представлении списка
            с страницы: addressbook/index.php
        Args:
            contact (Contact): объект Contact ./model/contact.py

        Returns:
            str: строка all_phones_from_home_page
            объекта Contact ./model/contact.py
        """
        return "\n".join(
            filter(
                lambda x: x != "",
                map(
                    lambda x: self.clear_email(x),
                    filter(
                        lambda x: x is not None,
                        [
                            contact.email,
                            contact.email_2,
                            contact.email_3,
                        ],
                    ),
                ),
            )
        )
