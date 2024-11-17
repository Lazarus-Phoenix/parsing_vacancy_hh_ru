''' Тесты для классов API с помощью pytest'''
import pytest
from src.api import HeadHunterAPI
from src.req_params import RequestParameter, SearchParameter


def test_api_key():
    """ Проверить чтение тестовых переменных окружения """
    hh = HeadHunterAPI(test_mode=True)
    assert hh._get_api_key() == 'TEST222'


def test_params():
    hh = HeadHunterAPI()
    search_prm = SearchParameter(keywords=['python', 'django'])
    req_prm = RequestParameter(count=100, page=0, archive=False, search=search_prm)

    assert hh._create_params(req_prm) == {
        "archive": False,
        "count": 100,
        "page": 0,
        "text": 'python django',
    }


def test_vacancies():
    hh = HeadHunterAPI()
    search_prm = SearchParameter(keywords=['100000'])
    req_prm = RequestParameter(count=100, page=0, archive=False, search=search_prm)
    hh_vacancies = hh.get_vacancies(request_params=req_prm)
    all_vacancies = len(hh_vacancies)
    assert hh_vacancies is not None
