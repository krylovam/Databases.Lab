import psycopg2
from scripts_sql import create_new_database, all_functions

def rootActivation():
    connection = psycopg2.connect(
        database="postgres",
        user="postgres",
        password='1234567890',
        host="127.0.0.1",
        port="5432"
    )
    connection.autocommit = True
    return connection

def userActivation():
    connection = psycopg2.connect(
        database="labdb",
        user='newuser',
        password='12345',
        host="127.0.0.1",
        port="5432"
    )
    connection.autocommit = True
    return connection

def activate_functions(connection):
    cursor = connection.cursor()
    cursor.execute(all_functions)
    cursor.close()
    connection.close()
    print("All functions are activated")

