from model.group import Group
import random
import string
import os.path
import json


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

data_file = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "../data/groups.json"
)
with open(data_file, "w", encoding="utf-8") as file:
    file.write(json.dumps(ddt, default=lambda x: x.__dict__, indent=2))
