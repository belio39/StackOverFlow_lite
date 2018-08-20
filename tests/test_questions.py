""""This are a module"""
import unittest
import os
import json

from app.views import create_app
from app.models import Questions, Answers

class StackOverflow_lite(unittest.TestCase):
    """This class represents Questions and Answers posted."""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.questions = {
            'Question': 'What is a flask restful api',
            'Date posted': 'datetime.datetime.now()'}
        self.answers = {
            'Question': 'Flask restful api',
            'Date posted': 'datetime.datetime.now()'}

    def test_post_question(self):
        """Testing posting a question."""
        response = self.client.post(
            '/api/v1/questions', data=json.dumps(self.questions), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_view_all_questions(self):
        """Test to view all questions."""
        response = self.client.get(
            '/api/v1/questions', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_one_question(self):
        """Test to get single question."""
        response = self.client.get(
            '/api/v1/questions/1', data=json.dumps(self.questions), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_post_answer_to_question(self):
        """Test to post answer"""
        response = self.client.post(
            '/api/v1/questions/1/answers', data=json.dumps(self.answers), content_type=
            'application/json')
        self.assertEqual(response.status_code, 200)

    def test_no_question(self):
        """Test to no question"""
        response = self.client.get(
            '/api/v1/questions/88', data=json.dumps(self.answers), content_type=
            'application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], "specific question not found")

if __name__ == "__main__":
    unittest.main()
