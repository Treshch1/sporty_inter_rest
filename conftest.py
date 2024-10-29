import pytest

from src.services import ApiClient


@pytest.fixture(scope='session')
def api_service():
    return ApiClient()
