from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
PATH_TO_JSON = BASE_DIR / "parsing_vacancy_hh_ru" / "data"
PATH_TO_TEST_JSON = BASE_DIR / "parsing_vacancy_hh_ru" / "tests"