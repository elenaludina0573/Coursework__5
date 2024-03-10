import psycopg2


def create_database(database_name, params):
    """Создание базы данных."""

    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()
    try:
        cur.execute(f'DROP DATABASE {database_name}')
    except psycopg2.errors.InvalidCatalogName:
        print('База данных не существует')

    cur.execute(f'CREATE DATABASE {database_name}')

    cur.close()
    conn.close()