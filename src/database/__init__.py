import sqlite3
from sqlite3 import Error


def init_connection(conn):
    cr = conn.cursor()
    cr.execute(
        """CREATE TABLE if not exists person(name text, class text, score text)""")
    conn.commit()


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        init_connection(conn)
    except Error as e:
        print(e)

    return conn


def create_person(conn, person):
    cur = conn.cursor()
    columns = ', '.join(person.keys())
    placeholders = ', '.join('?' * len(person))
    query = 'INSERT INTO person ({}) VALUES ({})'.format(columns, placeholders)
    values = [int(x) if isinstance(x, bool) else x for x in person.values()]
    cur.execute(query, values)
    conn.commit()
    return cur.lastrowid


def read_person(conn):
    conn.row_factory = sqlite3.Row
    query = 'SELECT * FROM person'
    data_array = conn.execute(query).fetchall()
    data_dict = [{k: item[k] for k in item.keys()} for item in data_array]
    return data_dict

def delete_person(conn):
    cur = conn.cursor()
    query = 'DELETE FROM person'
    cur.execute(query)
    conn.commit()