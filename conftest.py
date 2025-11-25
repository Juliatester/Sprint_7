import pytest
from data import register_new_courier_and_return_login_password
from generations import Generation

@pytest.fixture()
def base_url():
    """Возвращает базовый URL"""
    return "https://qa-scooter.praktikum-services.ru"


@pytest.fixture()
def create_unique_user():
    """Генерирует уникальные данные для пользователя"""
    user_data = {
        'login': Generation.login(),
        'password': Generation.password(),
        'firstName': Generation.first_name()
    }
    return user_data

@pytest.fixture()
def unique_user():
    """Создает уникального курьера и возвращает его данные"""
    result = register_new_courier_and_return_login_password()
    if result:
        login, password, first_name = result
        yield login, password, first_name
    else:
        pytest.skip("Не удалось создать курьера для теста")

@pytest.fixture
def api_client():
    from scooter_api import ScooterApi
    return ScooterApi()