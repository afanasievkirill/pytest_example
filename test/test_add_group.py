# -*- coding: utf-8 -*-
from pytest import mark

from model.group import Group
from utils.data_generator import DataGenerator

data = DataGenerator()

ddt = [
    Group(name=name, header=header, footer=footer)
    for name in ("", data.get_random_string("name", 10))
    for header in ("", data.get_random_string("header", 30))
    for footer in ("", data.get_random_string("footer", 20))
]


@mark.parametrize("group", ddt, ids=[repr(x) for x in ddt])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()

    app.group.create(group)

    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(
        new_groups, key=Group.id_or_max
    )
