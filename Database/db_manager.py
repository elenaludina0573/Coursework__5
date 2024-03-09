import psycopg2
from Database.getting_data_hh import params_db


class DBManager:

    """Класс для работы с информацией из Базы Данных"""

    @staticmethod
    def get_companies_and_vacancies_count():
        """Получает список всех компаний и количество вакансий у каждой компании."""
        with psycopg2.connect(dbname='HH_vacancy', **params_db) as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT company_name, COUNT(vacancy_name) from vacancies GROUP BY company_name')
                answer = cur.fetchall()
        conn.close()
        return answer

    @staticmethod
    def get_all_vacancies():
        """Получает список всех вакансий"""
        with psycopg2.connect(dbname='postgres', **params_db) as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT * from vacancies')
                answer = cur.fetchall()
        conn.close()
        return answer
