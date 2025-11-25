import pytest
import requests
import allure
from urls import Urls
from generations import Generation

class TestCreateOrder:

    @allure.title("Создание заказа с различными цветами")
    @pytest.mark.parametrize('color', [
        ["BLACK"],                   # Только черный цвет
        ["GREY"],                    # Только серый цвет
        ["BLACK", "GREY"],           # Черный и серый одновременно
        []                           # Цвет не выбран
    ])
    def test_create_order_with_color_parameterization(self, color):
        with allure.step("Генерация данных для заказа"):
            order_data = {
                "firstName": Generation.first_name(),
                "lastName": Generation.last_name(),
                "address": Generation.address(),
                "metroStation": Generation.nearest_stations()[0],
                "phone": Generation.phone(),
                "rentTime": Generation.rent_time(),
                "deliveryDate": Generation.delivery_date(),
                "comment": Generation.comment(),
                "color": color  # устанавливаем цвет из параметризованного набора
            }

        with allure.step("Отправляем POST-запрос на создание заказа"):
            response = requests.post(Urls.CREATE_ORDER, json=order_data)

        with allure.step("Проверяем успешность создания заказа"):
            assert response.status_code == 201
            assert 'track' in response.json(), "Нет трек-номера в ответе"
