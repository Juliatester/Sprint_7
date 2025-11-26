import pytest
from scooter_api import ScooterApi


@pytest.fixture
def api_client():
    """Возвращает клиент API для тестов"""
    return ScooterApi()


@pytest.fixture()
def unique_user():
    """Создает уникального курьера и возвращает его данные с удалением после теста"""
    api = ScooterApi()
    result = api.register_new_courier_and_return_login_password()
    if result:
        login, password, first_name = result
        yield login, password, first_name
        
        login_response = api.login_courier(login, password)
        if login_response.status_code == 200:
            courier_id = login_response.json()["id"]
            api.delete_courier(courier_id)
    else:
        pytest.skip("Не удалось создать курьера для теста")


@pytest.fixture
def create_and_delete_courier():
    """Фикстура для создания и автоматического удаления курьера после теста"""
    courier_data = {}
    yield courier_data
    
    if courier_data.get('login') and courier_data.get('password'):
        api = ScooterApi()
        login_response = api.login_courier(courier_data['login'], courier_data['password'])
        if login_response.status_code == 200:
            courier_id = login_response.json()["id"]
            api.delete_courier(courier_id)