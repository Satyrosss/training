import pytest


@pytest.fixture()
def fixture_function(request):
    print(f"\nI'm {request.scope} fixture")


@pytest.fixture(scope="class")
def fixture_class(request):
    print(f"\nI'm {request.scope} fixture")


@pytest.fixture(scope="module")
def fixture_module(request):
    print(f"\nI'm {request.scope} fixture")


@pytest.fixture(scope="session")
def fixture_session(request):
    print(f"\nI'm {request.scope} fixture")
