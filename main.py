from src.hh_api import HeadHunterAPI
from src.operations_on_vacancies import Vacancy
from src.save_vacancies import SaverJSON
from src.user import salary_range, top_n_salary


def user_input():
    """Функция взаимодействия с пользователем"""
    enter_the_search = input("Введите вакансию для поиска: ")
    print(f"Идет поиск вакансий {enter_the_search}\n")

    # поиск вакансий по запросу на hh.ru
    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies(enter_the_search)

    # сохранение полученных вакансий в json-файл
    saver = SaverJSON()
    saver.add_vacancies(hh_vacancies)

    # выбор пользователем действия
    if hh_vacancies:
        print("Выберите действие:")
        print("1. Показать все вакансии")
        print("2. Найти вакансии по названию")
        print("3. Показать вакансии от указанной зарплаты")
        print("4. Показать топ N вакансий по зарплате")
        print("5. Добавить вакансию")
        print("6. Удалить вакансию по url\n")

        # проверка корректности ввода пользователя
        try:
            action = int(input("Введите цифру от 1 до 6: "))
        except ValueError:
            print("Некорректный ввод. Выбрано действие 1")
            action = 1
        else:
            if action not in range(1, 7):
                print("Некорректный ввод. Выбрано действие 1")
                action = 1

    if action == 1:
        for vac in Vacancy.get_object_list(hh_vacancies):
            print(vac)
            print()

    elif action == 2:
        vacancy_name = input("Введите слово для поиска: ").lower()
        for vac in saver.get_inf(vacancy_name):
            print(vac)
            print()

    elif action == 3:
        try:
            salary_from = int(input("Укажите нижний порог зарплаты (целое число от 0): "))
        except ValueError:
            print("Некорректный ввод. Нижний порог не указан")
            salary_from = 0
        vacs_objects = Vacancy.get_object_list(hh_vacancies)
        for vac in salary_range(vacs_objects, salary_from):
            print(vac)
            print()

    elif action == 4:
        try:
            top_n = int(input("Введите количество вакансий для вывода в топ N: "))
        except ValueError:
            print("Количество вакансий должно быть целым числом")
            print("По умолчанию будет выведено 10 вакансий\n")
            top_n = 10

        if top_n > len(hh_vacancies):
            top_n = len(hh_vacancies) - 1

        vacs_objects = Vacancy.get_object_list(hh_vacancies)
        for vac in top_n_salary(vacs_objects, top_n):
            print(vac)
            print()

    elif action == 5:
        vacancy = Vacancy(input("Введите название: "), input("Введите ссылку на вакансию: "),
                          input("Введите требования к работе: "), input("Введите рабочие обязанности: "),
                          int(input("Введите зарплату: ")))
        saver.add_vacancy(vacancy)

    elif action == 6:
        url = input("Введите ссылку на вакансию: ")
        saver.del_vacancy(url)

    print("Работа программы завершена")


if __name__ == "__main__":
    user_input()