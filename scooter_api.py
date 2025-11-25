import requests
import allure
from urls import Urls


class ScooterApi:

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
        return requests.delete(f"{Urls.BASE_URL}/api/v1/courier/{courier_id}")

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

    @allure.step("Получить заказ по трек номеру")
    def get_order_by_track(self, track_number):
        params = {"t": track_number}
        return requests.get(Urls.GET_ORDER_BY_ID, params=params)

    @allure.step("Принять заказ")
    def accept_order(self, order_id, courier_id):
        params = {"courierId": courier_id}
        return requests.put(f"{Urls.ACCEPT_ORDER}{order_id}", params=params)

    @allure.step("Завершить заказ")
    def finish_order(self, order_id):
        return requests.put(f"{Urls.FINISH_ORDER}{order_id}")

    @allure.step("Отменить заказ")
    def cancel_order(self, track_number):
        payload = {"track": track_number}
        return requests.put(Urls.CANCEL_ORDER, json=payload)

    @allure.step("Получить количество заказов курьера")
    def get_courier_orders_count(self, courier_id):
        return requests.get(Urls.COURIER_ORDERS_COUNT.format(courier_id=courier_id))

    @allure.step("Пинг сервера")
    def ping_server(self):
        return requests.get(f"{Urls.BASE_URL}/api/v1/ping")

    @allure.step("Поиск станций метро")
    def search_stations(self, search_string):
        params = {"s": search_string}
        return requests.get(f"{Urls.BASE_URL}/api/v1/stations/search", params=params)