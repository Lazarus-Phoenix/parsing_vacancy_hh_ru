class SearchParameter:
    """ Параметры поиска """

    def __init__(self, title: bool = False, company: bool = False, full: bool = True, keywords: list = [],
                 and_parameter: bool = False):
        self.__title = title
        self.__company = company
        self.__full = full
        self.__keywords = keywords
        self.__and_parameter = and_parameter


    def get_hh_params(self):
        """ Получить парамтеры для запроса HH """
        params = dict()
        # формирование запроса
        # поиск везде по ключевым словам
        if self.__full:
            params['text'] = ' '.join(self.__keywords)
        else:
            pass
        return params


class RequestParameter:
    """ Параметры поиска вакансии """

    def __init__(self, count=100, page=0, archive=False, search=SearchParameter(title=False, company=False)):
        self.__count = count
        self.__page = page
        self.__archive = archive
        self.__search = search

    @property
    def count(self):
        """ Количество на одной странице """
        return self.__count

    @property
    def page(self):
        """ Количество страниц """
        return self.__page

    @property
    def archive(self):
        """ Смотреть архив """
        return self.__archive

    @property
    def search(self):
        """ Список ключевых слов """
        return self.__search

    def params(self, api_hh: bool = False):
        """ Формирование параметров для запроса """
        params = dict()
        if api_hh:
            for key, value in self.search.get_hh_params().items():
                # формирование запроса
                # поиск везде по ключевым словам
                params[key] = value
        params['count'] = self.__count
        params['page'] = self.__page
        params['archive'] = self.__archive
        return params
