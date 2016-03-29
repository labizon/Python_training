# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):  # -- Тестовый метод, принимающий fixture в качестве параметра и вызывающий
                          # -- в ней вспомагательные методы  --
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Test", header="test", footer="test"))
    app.session.logout()


def test_add_empty_group(app):  # -- Тестовый метод, принимающий fixture в качестве параметра и вызывающий
                                # -- в ней вспомагательные методы  --
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
