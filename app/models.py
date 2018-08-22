"""This is models.py file"""
questions = []
answers = []

class Questions():
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

class Answers():
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
