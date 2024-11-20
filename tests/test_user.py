from src.user import salary_range, sorting_by_salary, top_n_salary
from src.operations_on_vacancies import Vacancy


def test_salary_range(vacancies_objects):
    assert salary_range(vacancies_objects, 500000) == []
    assert salary_range(vacancies_objects, 100000) == [
        Vacancy("Разработчик", "https://hh", "требования", "обязанности", 100000)]
    assert salary_range(vacancies_objects, 0) == vacancies_objects
    assert salary_range([], 1000000) == []



def test_salary_range_empty_list(vacancies_objects):
    assert salary_range([], 1000000) == []


def test_salary_range_0(vacancies_objects):
    assert salary_range(vacancies_objects, 0) == vacancies_objects


def test_sorting_by_salary_same_salary():
    vacs = [
        Vacancy("Разработчик", "https://hh", "требования", "обязанности", 100000),
        Vacancy("Разработчик2", "https://hh2", "требования 2", "обязанности 2", 100000),
        Vacancy("Разработчик1", "https://hh1", "требования 1", "обязанности 1", 10000),
    ]
    res = sorting_by_salary(vacs)

    assert res == [
        Vacancy("Разработчик", "https://hh", "требования", "обязанности", 100000),
        Vacancy("Разработчик2", "https://hh2", "требования 2", "обязанности 2", 100000),
        Vacancy("Разработчик1", "https://hh1", "требования 1", "обязанности 1", 10000),
    ]


def test_sorting_by_salary_empty_list():
    res = sorting_by_salary([])
    assert res == []


def test_top_n_salary_empty_list():
    res = top_n_salary([], 2)
    assert res == []


def test_top_n_salary_top_n_0(vacancies_objects):
    res = top_n_salary(vacancies_objects, 0)
    assert res == []