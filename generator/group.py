import random
import string
import os.path
import jsonpickle
import getopt
import sys

from model.group import Group

try:
    opts, args = getopt.getopt(
        sys.argv[1:],
        "n:f",
        ["количество генерируемых групп.", "путь к файлу с данными."],
    )
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

f = "data/groups.json"

for o in opts:
    if o == "-f":
        f = a


def get_random_string(prefix, maxlen) -> str:
    """
        Функция генерирует строку состоящую из префикса и
        генерируемой часть из символов, чисел и пробелов
    Args:
        prefix str: префикс тестовой строки
        maxlen int: максимальная длина генерируемой строки

    Returns:
        str: строка с данными
    """
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join(
        [random.choice(symbols) for i in range(random.randrange(maxlen))]
    )


ddt = [
    Group(name=name, header=header, footer=footer)
    for name in ("", get_random_string("name", 10))
    for header in ("", get_random_string("header", 30))
    for footer in ("", get_random_string("footer", 20))
]

data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)


def generate_group_data():
    """
    Функция записывает сгенерированные элементы Group в JSON файл
    """
    with open(data_file, "w", encoding="utf-8") as file:
        jsonpickle.set_encoder_options("json", indent=2)
        file.write(jsonpickle.encode(ddt))
