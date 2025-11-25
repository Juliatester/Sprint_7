import pytest
import allure
from scooter_api import ScooterApi
from generations import Generation
from data import Messages
from data import register_new_courier_and_return_login_password


class TestCourierCreate:

    @allure.title("Курьера можно создать")
    def test_create_courier_success(self, api_client):
        login, password, first_name = Generation.login(), Generation.password(), Generation.first_name()
        
        response = api_client.create_courier(login, password, first_name)
        
        assert response.status_code == 201
        assert response.json() == Messages.SUCCESS

    @allure.title("Курьера можно создать без имени")
    def test_create_courier_without_first_name_success(self, api_client):
        login, password = Generation.login(), Generation.password()
        
        response = api_client.create_courier(login, password, "")
        
        assert response.status_code == 201
        assert response.json() == Messages.SUCCESS

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier_fails(self, api_client):
        """Проверяет что при дублировании логина возвращается 409"""
        login, password, first_name = Generation.login(), Generation.password(), Generation.first_name()
        
        first_response = api_client.create_courier(login, password, first_name)
        assert first_response.status_code == 201
        
        second_response = api_client.create_courier(login, password, first_name)
        assert second_response.status_code == 409
        assert "логин уже используется" in second_response.json().get("message", "")

    @allure.title("Создание курьера без логина возвращает ошибку")
    def test_create_courier_without_login_fails(self, api_client):
        response = api_client.create_courier("", "password", "name")
        assert response.status_code == 400

    @allure.title("Создание курьера без пароля возвращает ошибку")
    def test_create_courier_without_password_fails(self, api_client):
        response = api_client.create_courier("login", "", "name")
        assert response.status_code == 400

    @allure.title("Создание курьера с пустыми логином и паролем возвращает ошибку")
    def test_create_courier_with_empty_login_and_password_fails(self, api_client):
        response = api_client.create_courier("", "", "name")
        assert response.status_code == 400