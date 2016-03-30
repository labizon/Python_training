# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):  # -- Тестовый метод, принимающий fixture в качестве параметра и вызывающий
                          # -- в ней вспомагательные методы  --
    app.group.create(Group(name="Test", header="test", footer="test"))


def test_add_empty_group(app):  # -- Тестовый метод, принимающий fixture в качестве параметра и вызывающий
                                # -- в ней вспомагательные методы  --
    app.group.create(Group(name="", header="", footer=""))
