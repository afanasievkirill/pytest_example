import os.path
import jsonpickle
import mimesis
import getopt
import sys

from model.contact import Contact

try:
    opts, args = getopt.getopt(
        sys.argv[1:],
        "n:f",
        ["количество генерируемых групп.", "путь к файлу с данными."],
    )
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/contacts.json"

for o in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def get_random_data() -> Contact:
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


ddt = [get_random_data() for i in range(n)]

data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)


def generate_contact_data():
    """
    Функция записывает сгенерированные элементы Contact в JSON файл
    """
    with open(data_file, "w", encoding="utf-8") as file:
        jsonpickle.set_encoder_options("json", indent=2)
        file.write(jsonpickle.encode(ddt))
