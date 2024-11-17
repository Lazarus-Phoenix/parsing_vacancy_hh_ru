class Salary:
    """ Зарплата вакансии"""

    def __init__(self, salary_from: int = 0, salary_to: int = 0, agreement: bool = False):
        self.__from = salary_from
        self.__to = salary_to
        if self.__from == self.__to and self.__from == 0:
            self.__agreement = True
        else:
            self.__agreement = bool(agreement)

    @property
    def max_salary(self):
        """ Если зарплата не по договоренности вернуть максимальную сумму
        По договоренности вернуть 0
        """
        if self.is_agreement():
            return 0
        else:
            salary_list = [self.__from, self.__to]
            return max(salary_list)

    def is_agreement(self):
        """ Зарплата по договоренности """
        return self.__agreement

    def __eq__(self, other):
        """ Зарплаты равны
        Если обе по договоренности
        Если максимальные суммы равны
        """
        if isinstance(other, Salary):
            if self.is_agreement():
                return other.is_agreement()
            if self.max_salary == other.max_salary:
                return True
        return False

    def __lt__(self, other):
        """ Зарплата меньше """
        if isinstance(other, Salary) and not self.is_agreement():
            if self.max_salary < other.max_salary:
                return True
        return False

    def __gt__(self, other):
        """ Зарплата больше """
        if isinstance(other, Salary) and not self.is_agreement():
            if self.max_salary > other.max_salary:
                return True
        return False


class Vacancy:
    """ Описание найденной вакансии"""

    __Vacancies = []

    def __init__(self, title='', salary=Salary(agreement=True), link='', city='', company='', description='', platform=''):
        self.__title = title
        self.__salary = salary
        self.__link = link
        self.__city = city
        self.__company = company
        self.__description = description
        self.__platform = platform
        Vacancy.__Vacancies.append(self)

    def __eq__(self, other):
        """ Зарплаты равны """
        if isinstance(other, Vacancy):
            return self.__salary == other.__salary
        return False

    def __lt__(self, other):
        """ Зарплата меньше """
        if isinstance(other, Vacancy):
            return self.__salary < other.__salary
        return False

    def __gt__(self, other):
        """ Зарплата больше """
        if isinstance(other, Vacancy):
            return self.__salary > other.__salary
        return False

    @classmethod
    @property
    def vacancies(cls):
        """ Список вакансий """
        return cls.__Vacancies

    @property
    def title(self):
        """ Название вакансии """
        return self.__title

    @property
    def salary(self):
        """ Зарплата """
        return self.__salary

    @property
    def link(self):
        """ Ссылка на описание вакансии """
        return self.__link

    @property
    def city(self):
        """ Город """
        return self.__city

    @property
    def company(self):
        """ Наименование компании работодателя """
        return self.__company

    @property
    def description(self):
        """ Полное описание вакансии """
        return self.__description

    def __str__(self):
        agreement = 'По договоренности'
        return (f'Город:{self.city} Фирма:{self.company} Вакансия:{self.title} '
                f'Оплата:{agreement if self.salary.max_salary == 0 else self.salary.max_salary} '
                f'Ссылка:{self.link}')

    def get_json_data(self):
        """ Создать словарь из вакансии """
        vacancy_dict = dict()
        vacancy_dict['title'] = self.title
        vacancy_dict['link'] = self.link
        vacancy_dict['city'] = self.city
        vacancy_dict['company'] = self.company
        vacancy_dict['description'] = self.description
        vacancy_dict['platform'] = self.__platform
        if self.salary.is_agreement():
            vacancy_dict['salary_agreement'] = True
        vacancy_dict['salary'] = self.salary.max_salary
        return vacancy_dict