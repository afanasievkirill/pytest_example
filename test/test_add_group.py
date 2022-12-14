# -*- coding: utf-8 -*-
from pytest import mark

from model.group import Group
from data.groups import ddt


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


def test_add_group_from_json(app, json_groups):
    group = json_groups

    old_groups = app.group.get_group_list()

    app.group.create(group)

    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(
        new_groups, key=Group.id_or_max
    )


def test_add_group_from_data(app, data_groups):
    group = data_groups

    old_groups = app.group.get_group_list()

    app.group.create(group)

    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(
        new_groups, key=Group.id_or_max
    )
