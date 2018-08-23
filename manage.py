"""This is a model"""
import psycopg2
import os 

class Database(object):
    """This is a function"""
    def create_all(self, app):
        con = psycopg2.connect(
            f"dbname='{app.config.get('DATABASE_NAME')}'\
            user='dennis' password='12345'\
            host='localhost'")

        cur = con.cursor()

        # create a table

        cur.execute(
            "CREATE TABLE IF NOT EXISTS\
            users(id serial PRIMARY KEY,\
            username varchar, email varchar UNIQUE,\
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
