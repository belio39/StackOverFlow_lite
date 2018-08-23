"""This is models.py file"""
from manage import Database
import psycopg2
from flask import current_app

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    def save(self):
        con = psycopg2.connect(
            f"dbname='{current_app.config.get('DATABASE_NAME')}'\
            user='dennis' password='12345'\
            host='localhost'")
        
        cur = con.cursor()

        cur.execute("""INSERT INTO users(username, email, password)  VALUES('%s','%s','%s')"""
        %(self.username, self.email, self.password))

        con.commit()
        cur.close()
        con.close()

class register:
    def __init__(self, email, password):
        self.email = email
        self.password = password
    def save(self):
        con = psycopg2.connect(
            f"dbname='{current_app.config.get('DATABASE_NAME')}'\
            user='dennis' password='12345'\
            host='localhost'")
        
        cur = con.cursor()

        cur.execute("""INSERT INTO users(username, email, password)  VALUES('%s','%s','%s')"""
        %(self. self.email, self.password))

        con.commit()
        cur.close()
        con.close()        
    
    
class Questions:
    """This is a class"""
    counter = 0
    def __init__(self, question, date_posted):
        self.question = question
        self.date_posted = date_posted
        self._id = Questions.counter
        Questions.counter += 1

    def save(self):
        """This is method"""
        current_question = {
            "question": self.question,
            "date_posted": self.date_posted,
            "id": self._id
        }
        questions.append(current_question)
        return current_question
            

class Answers:
    """This is a class"""
    counter = 0

    def __init__(self, answer, date_posted):
        self.answer = answer
        self.date_posted = date_posted
        self._id = Answers.counter
        Answers.counter += 1

    def save(self):
        """This is a method"""
        current_answer = {
            "answer": self.answer,
            "date_posted": self.date_posted,
            "id": self._id
        }
        answers.append(current_answer)
        return current_answer

