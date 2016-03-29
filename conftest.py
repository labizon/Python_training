
import pytest
from fixture.application import Application


@pytest.fixture(scope = "session")
def app(request):
    fixture = Application() # -- Инициализация.  Создание fixture --
    request.addfinalizer(fixture.destroy) # -- Указание на то, как эта fixture должна быть разрушена  --
    return fixture