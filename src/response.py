import json
import logging
import allure


class AssertableResponse:
    def __init__(self, response):
        allure.attach(f"Request: URL={response.request.url}; BODY={response.request.body}", 'request.txt',
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Response: STATUS={response.status_code} BODY={json.dumps(response.json(), indent=4)}",
                      'response.txt', attachment_type=allure.attachment_type.TEXT)
        logging.info(f"Request: URL={response.request.url}; BODY={response.request.body}")
        logging.info(f"Response: STATUS={response.status_code} BODY={json.dumps(response.json(), indent=4)}")
        self._response = response

    @allure.step('Status code should be "{code}"')
    def status_code(self, code):
        logging.info(f"Assert: status code should be {code}")
        return self._response.status_code == code

    @allure.step
    def field(self, field):
        return self._response.json()[field]

    @allure.step('Response should have {condition}')
    def should_have(self, condition):
        logging.info(f"About to check {condition}")
        condition.match(self._response)
