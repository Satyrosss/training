import pytest
import random


@pytest.fixture()
def fixture_function():
    return random.randint(1, 10)


@pytest.fixture(scope="class")
def fixture_class():
    return 3


@pytest.fixture(scope="module")
def fixture_module():
    return 2


@pytest.fixture(scope="session")
def fixture_session():
    return 1

