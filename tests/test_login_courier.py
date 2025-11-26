import allure
import pytest
import requests
from urls import Urls
from generations import Generation
from data import Messages


class TestLoginCourier:

    @allure.title("Успешный логин курьера")
    def test_successful_login(self, unique_user):
        payload = {"login": unique_user[0], "password": unique_user[1]}
        response = requests.post(Urls.LOGIN_COURIER, json=payload)
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Логин без пароля")
    def test_login_without_password(self, unique_user):
        payload = {"login": unique_user[0], "password": ""}
        response = requests.post(Urls.LOGIN_COURIER, json=payload)
        assert response.status_code == 400

    @allure.title("Логин несуществующего курьера")
    def test_login_non_existent_courier(self):
        payload = {"login": Generation.login(), "password": Generation.password()}
        response = requests.post(Urls.LOGIN_COURIER, json=payload)
        assert response.status_code == 404

    @allure.title("Логин без логина")
    def test_login_without_login(self):
        payload = {"password": Generation.password()}
        response = requests.post(Urls.LOGIN_COURIER, json=payload)
        assert response.status_code == 400

    @allure.title("Логин с неверным паролем")
    def test_login_wrong_password(self, unique_user):
        payload = {"login": unique_user[0], "password": "incorrect_password"}
        response = requests.post(Urls.LOGIN_COURIER, json=payload)
        assert response.status_code == 404