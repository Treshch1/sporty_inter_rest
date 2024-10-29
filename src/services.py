import json

import allure
import requests

import config
from src.response import AssertableResponse


class ApiClient:
    def __init__(self):
        # self._base = ApiServiceBase()
        self.facts = FactsApiService()


class ApiServiceBase:

    def __init__(self, token=None):
        self.base_url = config.BASE_URL
        self._headers = {'Content-type': 'Application/json'}

    def _get(self, url, headers=None, params=None):
        headers = headers if headers else self._headers
        return requests.get(f'{self.base_url}{url}', params=params, headers=headers)

    def _post(self, url, body, headers=None):
        headers = headers if headers else self._headers
        return requests.post(f'{self.base_url}{url}', data=json.dumps(body), headers=headers)


class FactsApiService(ApiServiceBase):

    @allure.step("Request to /facts/random endpoint")
    def random(self, params=None):
        return AssertableResponse(self._get('/facts/random', params=params))
