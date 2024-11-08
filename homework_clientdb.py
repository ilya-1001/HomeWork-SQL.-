import psycopg2
from psycopg2 import Error
from psycopg2.sql import SQL, Identifier


def connect():
    try:
        conn = psycopg2.connect(database="clientdb",
                                user="postgres",
                                password="postgres",
                                host="localhost",
                                port="5432")
        cur = conn.cursor()
        return conn, cur
    except (Exception, psycopg2.Error) as error:
        print("Error while creating PostgreSQL table", error)


def create_client_table():
    conn, cur = connect()
    try:
        cur.execute("""
                    DROP TABLE if exists client CASCADE;
                    DROP TABLE if exists phone CASCADE;
                    """)
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS client(
                    id SERIAL PRIMARY KEY,
                    name varchar(40) not null,
                    surname varchar(60) not null,
                    email text not null unique
                    );
                    """)
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS phone(
                    id SERIAL PRIMARY KEY,
                    client_id integer references client(id),
                    phone_number varchar(20)
                    );
                    """)
        conn.commit()
    except (Exception, psycopg2.Error) as error:
        print('error', error)
    return 'create tables'


def add_a_new_client(name, surname, email, phone_number=None):
    conn, cur = connect()
    try:
        cur.execute("""
                    INSERT INTO client(name, surname, email)
                    VALUES(%s, %s, %s)
                    """, (name, surname, email))
        cur.execute("""
                    select * from client
                    where name=%s and surname=%s and email=%s
                    """, (name, surname, email))
        conn.commit()
    except (Exception, psycopg2.Error) as error:
        print('error', error)
    return cur.fetchall()


def add_phone(client_id, phone_number):
    conn, cur = connect()
    try:
        cur.execute("""
                    insert into phone(client_id, phone_number)
                    values(%s, %s)
                    """, (client_id,phone_number))
        cur.execute("""
                    select * from phone
                    where phone_number=%s
                    """, (phone_number, ))
        conn.commit()
    except (Exception, psycopg2.Error) as error:
        print('error', error)
    return cur.fetchone()


def change_client_data(id, name=None, surname=None, email=None, phone_number=None):
    conn, cur = connect()
    arg_list = {'name': name, "surname": surname, 'email': email}
    for key, arg in arg_list.items():
        if arg:
            cur.execute(SQL("""UPDATE client
                            SET {}=%s
                            WHERE id=%s""").format(Identifier(key)),
                        (arg, id))
    cur.execute("""
            SELECT * FROM client
            WHERE id=%s
            """, (id, ))
    conn.commit()
    return cur.fetchall()


def delete_phone(client_id, phone_number):
    conn, cur = connect()
    try:
        cur.execute("""
                    delete from phone
                    where client_id=%s
                    """,(client_id,))
        cur.execute("""
                    select * from phone
                    where client_id=%s
                    """, (client_id, ))
        conn.commit()
    except (Exception, psycopg2.Error) as error:
        print('error', error)
    return cur.fetchall()


def delete_client(id):
    conn, cur = connect()
    try:
        cur.execute("""
                    delete from client
                    where id=%s
                    """,(id,))
        cur.execute("""
                    select * from client
                    WHERE id=%s
                    """, (id, ))
        conn.commit()
    except (Exception, psycopg2.Error) as error:
        print('error', error)
    return cur.fetchall()


def find_client(name=None, surname=None, email=None, phone_number=None):
    conn, cur = connect()
    try:
        cur.execute("""
			        SELECT c.name, c.surname, c.email, p.phone_number From client c
			        JOIN phone p ON c.id = p.client_id
			        WHERE c.name=%s OR c.surname=%s OR c.email=%s OR p.phone_number=%s;
			        """, (name, surname, email, phone_number))
        conn.commit()
    except (Exception, psycopg2.Error) as error:
        print('error', error)
    return cur.fetchall()


print(connect())
print(create_client_table())
print(add_a_new_client('qwerty', 'asdfg', 'zxcv@jhgf.jh', '333666555'))
print(add_a_new_client('Ilya', 'Kobtsev', 'ikobtsev83@yandex.ru'))
print(add_phone(1, '99384766222 0'))
print(add_phone(2, '8999999874'))
print(add_phone(2, '321456789'))
print(change_client_data(2,'ilya', '', 'netology@yandex.ru'))
print(delete_phone(1, '99384766222 0'))
print(delete_client(1))
print(find_client('', 'Kobtsev'))

conn, cur = connect()
conn.close()
cur.close()
