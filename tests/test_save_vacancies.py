import json
import os

from config import DATA_DIR
from src.save_vacancies import SaverJSON
from src.operations_on_vacancies import Vacancy


def test_saver():
    saver = SaverJSON("test.json")
    vac = Vacancy("Разработчик", "https://hh", "требования", "обязанности", 0)

    saver.add_vacancy(vac)
    file = os.path.join(DATA_DIR, "test.json")

    with open(file, encoding="utf-8") as f:
        data = json.load(f)

    assert data == [
        {
            "name": "Разработчик",
            "url": "https://hh",
            "requirement": "требования",
            "responsibility": "обязанности",
            "salary": 0,
        }
    ]