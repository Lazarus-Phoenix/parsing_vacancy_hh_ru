import pytest
from src.operations_on_vacancies import Vacancy


@pytest.fixture
def vacancies_dict():
    vacs = [
        {
            "name": "Middle QA Engineer",
            "url": "https://hh.ru/vacancy/106954977",
            "requirement": "Желателен опыт написания автотестов (UI/API) на <highlighttext>python</highlighttext>. Владение английским языком на уровне B2 и готовность немного поговорить с...",
            "responsibility": "Функциональное тестирование frontend/backend (50/50). Разработка и написание тестовой/проектной документации. Заведение баг репортов.",
            "salary": 0
        },
        {
            "name": "Junior Python разработчик",
            "url": "https://hh.ru/vacancy/106571399",
            "requirement": "Базовые знания <highlighttext>Python</highlighttext>. Понимание ООП. Опыт работы с фреймворками (например, Django, Flask). Знание SQL. Базовые знания HTML, CSS, JavaScript. ",
            "responsibility": "Разработка и поддержка backend части приложения на <highlighttext>Python</highlighttext>. Работа с базами данных (например, PostgreSQL, MongoDB). Написание чистого, эффективного и хорошо...",
            "salary": 125000
        }]

    return vacs


@pytest.fixture
def vacancies_objects():
    vacs = [Vacancy("Разработчик", "https://hh", "требования", "обязанности", 100000),
            Vacancy("Разработчик1", "https://hh", "требования 1", "обязанности 1", 0)]

    return vacs