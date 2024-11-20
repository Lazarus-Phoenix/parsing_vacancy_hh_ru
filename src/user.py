from src.operations_on_vacancies import Vacancy


def salary_range(vacancies, salary_from):
    """Возвращает список вакансий с заданным значением зарплаты"""
    return [result for result in vacancies if result.salary >= salary_from]


def sorting_by_salary(vacancies):
    """Сортирует вакансии по зарплате"""
    return sorted(vacancies, key=lambda vacancy: vacancy.salary, reverse=True)


def top_n_salary(vacancies, top_n):
    """Возвращает топ N вакансий по зарплате"""
    sort_vacancies = sorting_by_salary(vacancies)
    return sort_vacancies[:top_n]
