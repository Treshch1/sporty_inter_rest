import abc
import jsonpath_rw
from hamcrest import assert_that


class Condition:

    def __init__(self):
        pass

    @abc.abstractmethod
    def match(self, response):
        pass


class StatusCodeCondition(Condition):

    def __init__(self, code):
        super().__init__()
        self._status_code = code

    def match(self, response):
        assert response.status_code == self._status_code

    def __repr__(self):
        return f'status code is {self._status_code}'


status_code = StatusCodeCondition


class BodyFieldCondition(Condition):
    def __init__(self, json_path, matcher):
        super().__init__()
        self._json_path = json_path
        self._matcher = matcher

    def match(self, response):
        json = response.json()
        matches = jsonpath_rw.parse(self._json_path).find(json)
        value = matches[0].value if len(matches) == 1 else [match.value for match in matches]
        assert_that(value, self._matcher)

    def __repr__(self):
        return f'body field {self._json_path} {self._matcher}'


body = BodyFieldCondition
