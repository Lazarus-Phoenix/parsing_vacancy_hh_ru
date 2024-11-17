''' Тесты для класса параметры запроса с помощью pytest'''
import pytest
from src.req_params import RequestParameter, SearchParameter


def test_search_parameter():
    search = SearchParameter(keywords=['python', 'django'])
    assert search.get_hh_params() == {
        'text': 'python django'
    }


def test_params():
    search = SearchParameter(keywords=['python', 'django'])
    request = RequestParameter(count=100, page=0, archive=False, search=search)
    assert request.count == 100
    assert request.page == 0
    assert not request.archive
    assert request.search == search
    assert request.params(api_hh=True) == {
        'count': 100,
        'page': 0,
        'archive': False,
        'text': 'python django'
    }