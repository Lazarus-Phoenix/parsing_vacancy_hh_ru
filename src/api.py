from abc import ABC, abstractmethod
from src.env import EnvParameter
from src.req_params import RequestParameter, SearchParameter
from src.vacancy import Vacancy, Salary
import requests


class API(ABC):
    """ Класс для описания абстрактных методов API """

    def __init__(self, test_mode=False):
        """ Инициализировать атрибуты """
        self.__test_mode = test_mode

    @property
    def test_mode(self):
        """ Флаг тестового режима """
        return self.__test_mode

    def _get_response_json(self, url=str(), params=dict(), headers=dict()):
        """ Получить ответ на запрос и распарсить JSON """
        rsp = requests.get(url=url, params=params, headers=headers)
        rsp_json = rsp.json()
        return rsp_json

    @abstractmethod
    def _get_api_key(self):
        """ Получить ключ из переменных окружения """
        pass

    @abstractmethod
    def _create_headers(self):
        """ Создать словарь с заголовком запроса """
        pass

    @abstractmethod
    def _create_params(self, request_params: RequestParameter):
        """ Создать словарь с параметрами запроса """
        pass

    @abstractmethod
    def get_vacancies(self, request_params: RequestParameter):
        """ Получить словарь с вакансиями """
        pass


class HeadHunterAPI(API):
    """ API для работы с вакансиями от headhunter.ru """

    def __init__(self, test_mode=False):
        """ Инициализировать атрибуты """
        super().__init__(test_mode)
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = self._create_headers()

    def _get_api_key(self):
        """ Получить api key для объекта без конструктора """
        if super().test_mode:
            return EnvParameter().api_key('TEST_HEADHUNTER_API_KEY')
        else:
            return EnvParameter().api_key('HEADHUNTER_API_KEY')

    def _create_headers(self):
        return {}

    def _create_params(self, request_params: RequestParameter):
        params = request_params.params(api_hh=True)
        return params

    def get_vacancies(self, request_params: RequestParameter):
        vacancies = self._get_response_json(url=self.__url, headers=self.__headers,
                                            params=self._create_params(request_params=request_params))
        # print(f'\n-----HeadHunter-----')
        hh_vacancies = []
        for vacancy in vacancies['items']:
            # название вакансии
            title = vacancy.get('name', 'Не указано')
            # ссылка на вакансию
            link = vacancy.get('alternate_url', 'Не указано')
            # город
            try:
                city = vacancy['area']['name']
            except KeyError:
                city = 'Не указано'

            # зарплата
            salary_object = vacancy.get('salary', None)
            if salary_object is None:
                salary = Salary(agreement=True)
            else:
                salary_from = salary_object.get('from', 0)
                if salary_from is None:
                    salary_from = 0
                salary_to = salary_object.get('to', 0)
                if salary_to is None:
                    salary_to = 0
                if salary_from == salary_to and salary_from == 0:
                    salary = Salary(agreement=True)
                else:
                    salary = Salary(salary_from=salary_from, salary_to=salary_to)
            # наименование компании работодателя
            company = 'Не указано'
            try:
                company_d = vacancy['employer']
                if company_d is not None:
                    company = company_d.get('name', 'Не указано')
            except KeyError:
                pass
            # описание вакансии
            description = 'Не указано'
            try:
                snippet = vacancy['snippet']
                description = snippet['requirement']
            except KeyError:
                pass

            vc = Vacancy(title=title, salary=salary, city=city, link=link, company=company, description=description,
                         platform='HH')
            hh_vacancies.append(vc)
        return hh_vacancies