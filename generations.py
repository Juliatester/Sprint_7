from faker import Faker
import random
import datetime

fake = Faker("ru_RU")


class Generation:

    @staticmethod
    def login():
        return fake.user_name()

    @staticmethod
    def password():
        return fake.password()

    @staticmethod
    def first_name():
        return fake.first_name()

    @staticmethod
    def last_name():
        return fake.last_name()

    @staticmethod
    def address():
        return fake.address()

    @staticmethod
    def nearest_stations(count=3):
        return random.sample(range(1, 11), count)

    @staticmethod
    def phone():
        return fake.phone_number()

    @staticmethod
    def rent_time():
        return random.randint(1, 7)

    @staticmethod
    def delivery_date():
        return (datetime.datetime.now() + datetime.timedelta(days=7)).strftime('%Y-%m-%d')

    @staticmethod
    def color():
        options = [
            ["BLACK"],
            ["GREY"],
            ["BLACK", "GREY"],
            []
        ]
        return random.choice(options)

    @staticmethod
    def comment():
        return fake.sentence()