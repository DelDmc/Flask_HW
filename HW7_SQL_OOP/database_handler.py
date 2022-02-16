import sqlite3


def execute_query(query, args=()):
    with sqlite3.connect('/home/del12dmc/PycharmProjects/Flask/HW7_SQL_OOP/chinook.db') as connection:
        cursor = connection.cursor()
        cursor.execute(query, args)
        connection.commit()
        records = cursor.fetchall()
    return records

