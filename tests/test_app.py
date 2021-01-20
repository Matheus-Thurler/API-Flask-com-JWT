import requests


class TestHoteis:
    url_base_hotels = "http://127.0.0.1:5000/hotels"
    url_base_users = "http://127.0.0.1:5000/users"

    create_user = {"login" : "matheus thurler4", "password" : "123"}

    def test_get_hoteis(self):
        hoteis = requests.get(url=self.url_base_hotels)

        assert hoteis.status_code == 200


    def test_get_hotel(self):
        hotel = requests.get(url=f'{self.url_base_hotels}/marvel')

        assert hotel.status_code == 200


    def test_get_users(self):
        users = requests.get(url=f'{self.url_base_users}/3')

        assert users.status_code == 200