from psycopg2 import connect, OperationalError, DatabaseError

USER = "postgres"
HOST = "localhost"
PASSWORD = "12345"
CREATE_DB_SQL = 'CREATE DATABASE communicator_db ;'
CREATE_TABLE_USERS = """CREATE TABLE users(
                        id serial PRIMARY KEY,
                        username varchar(255),
                        hashed_password varchar(80)
                        );"""
CREATE_TABLE_MESSAGES = """CREATE TABLE messages(
                            id serial PRIMARY KEY,
                            from_id int NOT NULL,
                            to_id int NOT NULL,
                            creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            text varchar(255),
                            FOREIGN KEY (from_id) REFERENCES users(id),
                            FOREIGN KEY (to_id) REFERENCES users(id)
                            );"""


def create_sql_db(sql_code):
    try:
        cnx = connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
        )
        cnx.autocommit = True
        cursor = cnx.cursor()

        try:
            cursor.execute(sql_code)
            print('Baza danych stworzona!')
        except DatabaseError as e:
            print('Podana baza danych już istnieje-', e)
        cnx.close()
    except OperationalError as e:
        print(e)


def create_table(sql_code):
    try:
        cnx = connect(
            user=USER,
            password=PASSWORD,
            host=HOST,
            database='communicator_db'
        )
        cnx.autocommit = True
        cursor = cnx.cursor()
        try:
            cursor.execute(sql_code)
            print('Tabela stworzona!')
        except DatabaseError as e:
            print('Podana tabela już istnieje-', e)
        cnx.close()
    except OperationalError as e:
        print(e)


create_sql_db(CREATE_DB_SQL)
create_table(CREATE_TABLE_USERS)
create_table(CREATE_TABLE_MESSAGES)
