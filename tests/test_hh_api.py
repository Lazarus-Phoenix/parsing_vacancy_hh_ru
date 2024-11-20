from src.hh_api import HeadHunterAPI


def test_head_hunter_api():
    api = HeadHunterAPI()
    assert api.url == "https://api.hh.ru/vacancies"
    vacs = api.get_vacancies("python")
    assert len(vacs) == 2000