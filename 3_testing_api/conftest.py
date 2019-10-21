import pytest
import requests


class SetRequest:

    def __init__(self, base_address):
        self.base_address = base_address

    def get(self, path='/', params=None, headers=None):
        url = self.base_address + path
        return requests.get(url=url, params=params, headers=headers)

    def post(self, path='/', params=None, headers=None, data=None):
        url = self.base_address + path
        return requests.post(url=url, params=params, headers=headers, data=data)


@pytest.fixture()
def request_dogs():
    return SetRequest(base_address="https://dog.ceo/api")


@pytest.fixture()
def request_breweries():
    return SetRequest(base_address="https://api.openbrewerydb.org/breweries")


@pytest.fixture()
def request_jsonplaceholder():
    return SetRequest(base_address="https://jsonplaceholder.typicode.com/")


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://ya.ru",
        help="This is request url"
    )


@pytest.fixture()
def request_url(request):
    return SetRequest(base_address=request.config.getoption("--url"))
