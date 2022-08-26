import psycopg2


def create_db_client(conn):
    cur.execute(""" 
     CREATE TABLE IF NOT EXISTS client
        (id SERIAL PRIMARY KEY,
         first_name TEXT NOT NULL,
         last_name TEXT NOT NULL,
         email TEXT NOT NULL,
     );
     """)
    conn.commit()


def create_db_phones(conn):
    cur.execute("""
    CREATE TABLE IF NOT EXISTS phones
       (id SERIAL PRIMARY KEY  RELATED TO client id,
       phones TUPLE
    );
    """)
    conn.commit()


def add_client(conn, first_name, last_name, email):
    cur.execute("""            
    INSERT INTO client(first_name) VALUES('first_name');
    INSERT INTO client(last_name) VALUES('last_name')
    INSERT INTO client(email) VALUES('email');
    """, (first_name, last_name, email, ))
    conn.commit()


def add_phone(conn, phones_id, phones):
    cur.execute("""
        INSERT INTO phones(phones) VALUES('phones');
        """, (phones_id, phones))
    print(cur.fetchone())


def change_client(conn, client_id, first_name=None, last_name=None, email=None):
    cur.execute("""
    INSERT INTO client(first_name, last_name, email) VALUES('','','');
    """, (client_id, first_name, last_name, email))
    conn.commit()


def delete_client(conn, client_id):
    cur.execute("""
        DELETE FROM client WHERE id=%s;
        """, (client_id,))
    print(cur.fetchall())


def delete_phone(conn, phones_id, phones):
    cur.execute("""
        DELETE FROM phones WHERE id=%s;
        """, (phones, phones_id))
    print(cur.fetchall())


def find_client(conn, first_name=None, last_name=None, email=None):
    cur.execute("""
        SELECT id FROM course WHERE first name='', last name='', email='' ;
        """, (first_name, last_name, email))
    print(cur.fetchone())


with psycopg2.connect(database="postgres", user="postgres", password="password") as conn:
    with conn.cursor() as cur:

        if __name__ == '--main---':
            create_db_client(conn)

        if __name__ == '--main---':
            create_db_phones(conn)

        if __name__ == '--main---':
            add_client(conn, first_name='Vasya', last_name='Pupkin', email='asd@yandex.ru')

        if __name__ == '--main---':
            add_client(conn, first_name='Vaya', last_name='Pupin', email='ad@yandex.ru')

        if __name__ == '--main---':
            add_phone(conn, phones=(22 - 33 - 44), phones_id=1)

        if __name__ == '--main---':
            delete_phone(conn, phones=(12 - 12 - 12), phones_id=1)

        if __name__ == '--main---':
            change_client(conn, client_id=1, first_name='Basya', last_name='Pupkin', email='asad@yandex.ru')

        if __name__ == '--main---':
            find_client(conn, first_name='Basya', last_name='Pupkin', email='asad@yandex.ru')

        if __name__ == '--main---':
            delete_client(conn, client_id=1)

conn.close()
