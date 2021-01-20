
import requests
import pytest


class TestHoteis:
    url_base = "http://127.0.0.1:5000/hotels"

    def test_get_hoteis(self):
        hoteis = requests.get(url=self.url_base)

        assert hoteis.status_code == 200