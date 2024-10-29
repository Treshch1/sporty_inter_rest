from src.conditions import status_code, body
from hamcrest import equal_to, has_length, greater_than


def test_can_access_me_api(api_service):
    response = api_service.user.get_me()
    response.should_have(status_code(200))
    response.should_have(body('$.full_name', equal_to('Owner Stage')))


def test_another_access_me_api(api_service):
    response = api_service.user.get_me()
    response.should_have(status_code(200))
    response.should_have(body('$.is_main_company_user', equal_to(True)))
    response.should_have(body('$.roles', has_length(greater_than(0))))
    # assert response.field('is_main_company_user')
    # assert len(response.field('roles'))
