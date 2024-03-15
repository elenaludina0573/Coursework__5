from Database.getting_data_hh import HH_api_db
from config import config
from Database.db_manager import DBManager
from Database.utils import create_database, create_table


def main():
    params_db = config()
    create_database('HH_parser', params_db)
    create_table(params_db)
    db_vacancies = HH_api_db()
    db_vacancies.employers_to_db()
    db_vacancies.vacancies_to_db()
    while True:
        task = input(
            "Введите 1, чтобы получить список всех компаний и количество вакансий у каждой компании\n"
            "Введите 2, чтобы получить список всех вакансий с указанием названия компании, "
            "названия вакансии и зарплаты и ссылки на вакансию\n"
            "Введите 3, чтобы получить среднюю зарплату по вакансиям\n"
            "Введите 4, чтобы получить список всех вакансий, у которых зарплата выше средней по всем вакансиям\n"
            "Введите 5, чтобы получить список всех вакансий, в названии которых содержатся переданные в метод слова\n"
            "Введите Стоп, чтобы завершить работу\n"
        )

        if task == "Стоп":
            break
        elif task == '1':
            print(DBManager.get_companies_and_vacancies_count())
            print()
        elif task == '2':
            print(DBManager.get_all_vacancies())
            print()
        elif task == '3':
            print(DBManager.get_avg_salary())
            print()
        elif task == '4':
            print(DBManager.get_vacancies_with_higher_salary())
            print()
        elif task == '5':
            keyword = input('Введите ключевое слово: ')
            print(DBManager.get_vacancies_with_keyword(keyword))
            print()
        else:
            print('Неправильный запрос')


if __name__ == '__main__':
    main()
    # print(DBManager.get_all_vacancies())
    # DBManager.get_avg_salary()
    # print(DBManager.get_vacancies_with_keyword('продавец'))
    # DBManager.get_companies_and_vacancies_count()
    # DBManager.get_vacancies_with_higher_salary()
