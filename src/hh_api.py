from http.client import responses

import requests

from abc import ABC, abstractmethod


class Parser(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями"""
    @abstractmethod
    def get_vacancies(self, keyword):
        pass

class HeadHunterAPI(Parser):
    """Класс для работы с API сервиса с вакансиями"""

    def __init__(self):
        """Инициализатор класса HeadHunterAPI"""
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies = []

    @property
    def url(self) -> str:
        """Возвращает cвойство url"""
        return self.__url

    def __api_connect(self):
        """Подключение к API сервиса с вакансиями"""
        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        if response.status_code == 200:
            return response

        print("Ошибка получения данных")

    def get_vacancies(self, keyword):
        """Получение вакансий по кодовому слову"""
        self.__params['text'] = keyword
        while self.__params.get('page') != 20:
            response = self.__api_connect()
            if response:
                vacancies = response.json()['items']
                self.__vacancies.extend(vacancies)
                self.__params['page'] += 1
            else:
                break

        vacancies_list = []

        if self.__vacancies:
            #получение списка словарей
            for vacancy in self.__vacancies:
                name = vacancy.get("name")
                url = vacancy.get("alternate_url")
                requirement = vacancy.get("snippet").get("requirement")
                responsibility = vacancy.get("snippet").get("responsibility")

                if vacancy.get("salary"):
                    if vacancy.get("salary").get("to"):
                        salary = vacancy.get("salary").get("to")
                    elif vacancy.get("salary").get("from"):
                        salary = vacancy.get("salary").get("from")
                else:
                    salary = 0

                result = {"name": name, "url": url, "requirement": requirement, "responsibility": responsibility, "salary": salary}

                vacancies_list.append(result)

        return vacancies_list