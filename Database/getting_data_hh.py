import os
import requests
import psycopg2
from config import config

params_db = config()


class HH_api_db:

    """Класс для работы с API HH.ru и заполнение таблиц в BD"""

    employers_dict = {'МегаФон': '3127',
                      'МТС': '3776',
                      'билайн': '4934',
                      'СБЕР': '3529',
                      'Банк ВТБ (ПАО)': '4181',
                      'Тинькофф': '78638',
                      'АШАН Ритейл Россия': '54979',
                      '2ГИС': '64174',
                      'Газпромбанк': '3388',
                      'Ozon': '2180'}

    @staticmethod
    def get_request(self, employer_id) -> dict:
        """Запрос списка работодателей, при наличии вакансий и заработной платы"""
        params = {
            "page": 1,
            "per_page": 100,
            "employer_id": employer_id,
            "only_with_salary": True,
            "area": 113,
            "only_with_vacancies": True
        }
        return requests.get("https://api.hh.ru/vacancies/", params=params).json()['items']


