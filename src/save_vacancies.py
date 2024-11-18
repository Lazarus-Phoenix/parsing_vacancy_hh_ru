import json
import os
import os.path

from abc import ABC, abstractmethod
from json import JSONDecodeError

from config import DATA_DIR
from src.operations_on_vacancies import Vacancy


class Saver(ABC):
    """Абстрактный класс для реализации операций над вакансиями"""

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_inf(self, word):
        pass

    @abstractmethod
    def del_vacancy(self, url):
        pass


class SaverJSON(Saver):
    """Класс для сохранения данных в json файл"""

    def __init__(self, filename="vacancies.json"):
        """Инициализатор класса SaverJSON"""
        self.__file_path = os.path.join(DATA_DIR, filename)

    def __save_to_file(self, vacancies):
        """Сохраняет данные в json файл"""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(vacancies, f, ensure_ascii=False)

    def __read_file(self):
        """Считывает данные из json файла"""
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []
        except JSONDecodeError:
            data = []

        return data

    def add_vacancy(self, vacancy):
        """Добавляет вакансию в файл"""
        vacancies_list = self.__read_file()
        if vacancy.url not in [result["url"] for result in vacancies_list]:
            vacancies_list.append(vacancy.to_dict())
            self.__save_to_file(vacancies_list)

    def add_vacancies(self, vacancies):
        """Добавляет вакансии в файл"""
        self.__save_to_file(vacancies)

    def del_vacancy(self, url):
        """Удаляет вакансию из файла"""
        vacancies_list = self.__read_file()
        for index, result in enumerate(vacancies_list):
            if result["url"] == url:
                vacancies_list.pop(index)

        self.__save_to_file(vacancies_list)

    def get_inf(self, word):
        """Фильтрует список вакансий по ключевому слову"""
        filtered_vacancies = []

        for result in self.__read_file():
            if word in result.get("name").lower():
                filtered_vacancies.append(result)

        return Vacancy.get_object_list(filtered_vacancies)
