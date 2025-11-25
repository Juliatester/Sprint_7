
class Urls:
    BASE_URL = "https://qa-scooter.praktikum-services.ru"

    # Для заказа
    CREATE_ORDER = f"{BASE_URL}/api/v1/orders"
    GET_LIST_ORDER = f"{BASE_URL}/api/v1/orders"
    FINISH_ORDER = f"{BASE_URL}/api/v1/orders/finish/"
    CANCEL_ORDER = f"{BASE_URL}/api/v1/orders/cancel"
    GET_ORDER_BY_ID = f"{BASE_URL}/api/v1/orders/track"
    ACCEPT_ORDER = f"{BASE_URL}/api/v1/orders/accept/"

    # Для курьера 
    CREATE_COURIER = f"{BASE_URL}/api/v1/courier"
    LOGIN_COURIER = f"{BASE_URL}/api/v1/courier/login"
    COURIER_ORDERS_COUNT = f"{BASE_URL}/api/v1/courier/{{courier_id}}/ordersCount"
