import psycopg2
from config import basevars


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print(f'Connecting to the PostgreSQL database... {basevars.conn_string}')
        conn = psycopg2.connect(dbname=basevars.database, user=basevars.user, password=basevars.password,
                                host=basevars.host, port=5432, options='-c search_path=telegram_crawler_demo_access')

        # create a cursor
        cur = conn.cursor()

	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT * from channel')

        # display the PostgreSQL database server version
        db_version = cur.fetchall()

        print(db_version)

	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()
