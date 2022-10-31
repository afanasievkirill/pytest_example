from model.contact import Contact
import mimesis
from selenium.webdriver.support.ui import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def go_to_contact_page(self):
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

    def edit_first(self, contact: Contact, index: int):
        self.edit_by_index(contact, index)

    def edit_by_index(self, contact: Contact, index: int):
        wd = self.app.wd
        self.go_to_contact_page()
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()
        self.__fill_conctact_form(contact)
        wd.find_element_by_xpath("(//input[@value='Update'][2])").click()
        wd.find_element_by_link_text("home").click()
        self.contact_cache = None

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
        wd.find_element_by_name("phone2").send_keys(contact.home)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)

    def get_data(self):
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
            home=mimesis.Address().address(),
            notes=mimesis.Text().text(),
        )
        return contact

    contact_cache = None

    def get_contact_list(self):
        """
            Функция проверяет кэш, в случае его отсутсвия
            пербирает записи на странице:
            http://localhost/addressbook/index.php и возвращает их список.
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
                self.contact_cache.append(
                    Contact(firstname=firstname, lastname=lastname, id=id)
                )
        return self.contact_cache
