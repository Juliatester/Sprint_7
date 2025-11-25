import pytest
import allure
from scooter_api import ScooterApi
from urls import Urls
from generations import Generation




class TestGetListOrders:

    @allure.title("Получение списка заказов возвращает список")
    def test_get_list_of_orders(self, api_client):
        with allure.step("Отправляем запрос на получение списка заказов"):
            response = api_client.get_orders_list()

        with allure.step("Проверяем успешность получения списка заказов"):
            assert response.status_code == 200, "Ошибка при получении списка заказов"

        with allure.step("Проверяем, что ответ содержит список заказов"):
            assert isinstance(response.json().get('orders', []), list), "Полученный ответ не содержит список заказов"