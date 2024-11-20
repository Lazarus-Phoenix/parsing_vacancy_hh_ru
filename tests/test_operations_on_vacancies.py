from src.operations_on_vacancies import Vacancy


def test_vacancy_init():
    vac = Vacancy("Разработчик", "https://hh", "требования", "обязанности", 0)
    assert vac.name == "Разработчик"
    assert vac.url == "https://hh"
    assert vac.requirement == "требования"
    assert vac.responsibility == "обязанности"
    assert vac.salary == 0


def test_get_object_list(vacancies_dict):
    vacs = Vacancy.get_object_list(vacancies_dict)
    assert len(vacs) == 2
    assert vacs[0].name == "Middle QA Engineer"
    assert vacs[1].salary == 125000


def test_get_object_list_empty_list():
    vacs = Vacancy.get_object_list([])
    assert vacs == []


def test_vacancy_str_salary_0():
    vac = Vacancy("Разработчик", "https://hh", "требования", "обязанности", 0)
    assert (
        str(vac)
        == "Разработчик (Зарплата: не указана). \nТребования: требования.\nОбязанности: обязанности.\nСсылка на вакансию: https://hh"
    )


def test_vacancy_eq(vacancies_objects):
    vac = Vacancy("Разработчик", "https://hh", "требования", "обязанности", 0)
    assert vacancies_objects[0] != vacancies_objects[1]
    assert vacancies_objects[1] == vac


def test_vacancy_to_dict(vacancies_objects):
    vac = vacancies_objects[0]
    assert vac.to_dict() == {
        "name": "Разработчик",
        "url": "https://hh",
        "requirement": "требования",
        "responsibility": "обязанности",
        "salary": 100000,
    }

    vac = Vacancy("Разработчик", "https://hh", "требования", "обязанности", 0)
    assert vac.to_dict() == {
        "name": "Разработчик",
        "url": "https://hh",
        "requirement": "требования",
        "responsibility": "обязанности",
        "salary": 0,
    }
