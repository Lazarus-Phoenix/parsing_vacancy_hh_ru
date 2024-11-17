import json
from abc import ABC, abstractmethod
import os


class Downloader(ABC):
    """ Класс для выгрузки списка вакансий """

    def __init__(self, encoding='utf-8'):
        self.__encoding = encoding

    @abstractmethod
    def save_file(self, filename=''):
        pass

    @property
    def encoding(self):
        return self.__encoding


class JSONDownloader(Downloader):
    """ Класс для сохранения данных в JSON файл """

    def __init__(self, data):
        self.__data = data
        super().__init__()

    def save_file(self, filename=''):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        root_dir = os.path.split(current_dir)[0]
        filepath = os.path.join(root_dir, os.path.normpath('data'), filename)
        if os.path.isdir(root_dir):
            with open(file=filepath, mode='w', encoding=super().encoding) as file:
                json.dump(self.__data, file, ensure_ascii=False, indent=4)