"""This is a model"""
import psycopg2

def database(app):
    """This is a function"""

    con = psycopg2.connect(
        "dbname='stack_over_flow'\
        user='dennis' password='12345'\
        host='localhost'")

    cur = con.cursor()

    # create a table

    cur.execute(
        "CREATE TABLE IF NOT EXISTS\
        users(id serial PRIMARY KEY,\
        name varchar, email varchar UNIQUE,\
        password varchar);")

    cur.execute("""CREATE TABLE IF NOT EXISTS questions(
            id serial PRIMARY KEY, date_posted varchar, questions varchar, user_id INT , 
            FOREIGN KEY (user_id) REFERENCES users(id)
        );""")

    cur.execute("""CREATE TABLE IF NOT EXISTS answers(
            id serial PRIMARY KEY, date_posted varchar, answers varchar, user_id INT , 
            FOREIGN KEY (user_id) REFERENCES users(id)
        );""")

    print("Database has been connected")
    con.commit()
