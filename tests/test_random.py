import pytest
from hamcrest import equal_to, has_length, greater_than, instance_of

from src.conditions import status_code, body


def test_random_fact_default_animal_type_is_cat_and_1_fact(api_service):
    response = api_service.facts.random()
    response.should_have(status_code(200))
    response.should_have(body('$', instance_of(dict)))
    response.should_have(body('$.type', equal_to('cat')))


@pytest.mark.parametrize('animal_type', ('cat', 'dog'))
def test_random_fact_animal_type_is_dog(api_service, animal_type):
    response = api_service.facts.random(params={'animal_type': animal_type})
    response.should_have(status_code(200))
    response.should_have(body('$.type', equal_to(animal_type)))


@pytest.mark.parametrize('amount', (0, 2, 500))
def test_random_fact_amount_valid_params(api_service, amount):
    response = api_service.facts.random(params={'amount': amount})
    response.should_have(status_code(200))
    response.should_have(body('$', instance_of(list)))
    response.should_have(body('$', has_length(amount)))


def test_random_fact_amount_invalid_params(api_service):
    response = api_service.facts.random(params={'amount': 501})
    response.should_have(status_code(405))
    response.should_have(body('$.message', equal_to('Limited to 500 facts at a time')))


def test_random_fact_is_returned(api_service):
    response_1 = api_service.facts.random()
    response_2 = api_service.facts.random()
    assert response_1.field('text') != response_2.field('text')
