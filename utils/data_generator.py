import random, string
import mimesis

from model.contact import Contact


class DataGenerator:
    def get_random_string(self, prefix, maxlen) -> str:
        symbols = string.ascii_letters + string.digits + " " * 10
        return prefix + "".join(
            [random.choice(symbols) for i in range(random.randrange(maxlen))]
        )

    def get_random_data(self) -> Contact:
        """
            Функция создает объект с рандомными данными
            для использования в тестах с помощью библиотеки mimesis.
        Returns:
            Contact: Объект Contact ./model/contact.py
        """
        return Contact(
            firstname=mimesis.Person().first_name(),
            lastname=mimesis.Person().last_name(),
            middlename=mimesis.Person().full_name(),
            nickname=mimesis.Food().fruit(),
            photo_path="\README.md",
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
