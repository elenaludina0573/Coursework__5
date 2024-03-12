# ** Курсовая работа. Работа с базами данных **
>###### main.py - файл запуска программы

🧑🏻‍💻 В рамках проекта вам необходимо получить данные о компаниях и вакансиях с сайта [hh.ru](hh.ru), спроектировать таблицы в БД PostgreSQL и загрузить полученные данные в созданные таблицы.

## Для работы с проектом необходимо

 * Создать файл  с названием ___database.ini___, который заполняется следующим образом:
   [postgresql]
   host=YourHost
   user=YourUser
   password=YourPassword
   port=YourPort
 * Словарь с данными для подключения к БД мы получаем из функции, находящейся в файле ___config.py___:
'''
from configparser import ConfigParser

def config(filename="database.ini", section="postgresql"):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} is not found in the {1} file.'.format(section, filename))
    return db
'''

## Основные шаги проекта

  * Получить данные о работодателях и их вакансиях с сайта [hh.ru](hh.ru). Для этого используйте публичный API [hh.ru](hh.ru) и библиотеку ___requests___.
  * Выбрать не менее 10 интересных вам компаний, от которых вы будете получать данные о вакансиях по API.
  * Спроектировать таблицы в БД Postgres для хранения полученных данных о работодателях и их вакансиях. Для работы с БД используйте библиотеку psycopg2.
  * Реализовать код, который заполняет созданные таблицы в БД Postgres данными о работодателях и их вакансиях.
  * Создать класс DBManager для работы с данными в БД.

## Класс DBManager

Создайте класс DBManager, который будет подключаться к БД Postgres и иметь следующие методы:

  * get_companies_and_vacancies_count(): получает список всех компаний и количество вакансий у каждой компании.
  * get_all_vacancies(): получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
  * get_avg_salary(): получает среднюю зарплату по вакансиям.
  * get_vacancies_with_higher_salary(): получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
  * get_vacancies_with_keyword(): получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”.

Класс DBManager должен использовать библиотеку ___psycopg2___ для работы с БД.
