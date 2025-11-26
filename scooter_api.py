import requests
import allure
import random
import string
from urls import Urls


class ScooterApi:

    @allure.step("Зарегистрировать нового курьера")
    def register_new_courier_and_return_login_password(self):
        """Метод регистрации нового курьера возвращает список из логина и пароля
        Если регистрация не удалась, возвращает пустой список"""
        
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login_pass = []

        # генерируем логин, пароль и имя курьера
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # отправляем запрос на регистрацию курьера
        response = requests.post(Urls.CREATE_COURIER, json=payload)

        # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        return login_pass

    @allure.step("Создать курьера")
    def create_courier(self, login, password, first_name):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return requests.post(Urls.CREATE_COURIER, json=payload)

    @allure.step("Логин курьера")
    def login_courier(self, login, password):
        payload = {
            "login": login,
            "password": password
        }
        return requests.post(Urls.LOGIN_COURIER, json=payload)

    @allure.step("Удалить курьера")
    def delete_courier(self, courier_id):
        return requests.delete(Urls.DELETE_COURIER.format(courier_id=courier_id))

    @allure.step("Создать заказ")
    def create_order(self, order_data):
        return requests.post(Urls.CREATE_ORDER, json=order_data)

    @allure.step("Получить список заказов")
    def get_orders_list(self, courier_id=None, nearest_station=None, limit=30, page=0):
        params = {
            "limit": limit,
            "page": page
        }
        if courier_id:
            params["courierId"] = courier_id
        if nearest_station:
            params["nearestStation"] = nearest_station
        return requests.get(Urls.GET_LIST_ORDER, params=params)