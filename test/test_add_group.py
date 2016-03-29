# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application() # -- Инициализация.  Создание fixture --
    request.addfinalizer(fixture.destroy) # -- Указание на то, как эта fixture должна быть разрушена  --
    return fixture


def test_add_group(app):  # -- Тестовый метод, принимающий fixture в качестве параметра и вызывающий
                          # -- в ней вспомагательные методы  --
    app.login(username="admin", password="secret")
    app.create_group(Group(name="Test", header="test", footer="test"))
    app.logout()


def test_add_empty_group(app):  # -- Тестовый метод, принимающий fixture в качестве параметра и вызывающий
                                # -- в ней вспомагательные методы  --
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
