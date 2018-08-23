"""This is a module"""

import os
import unittest
import json

from app.views import create_app

class StackOverFlow_lite(unittest.TestCase):
 def setUp(self):
    self.app = create_app(config_name="testing")
    self.client = self.app.test_client
    self.user_data = {
      'email': 'test@example.com',
      'password': 'test_password'
      }

    with self.app.app_context():
      db.session.close()
      db.drop_all()
      db.create_all()

  def test_registration(self):
    """Test user registration"""
    res = self.client().post('/auth/register', data=self.user_data)
    result = json.loads(res.data.decode())
    asert.assertEqual(result['message'], "You are registered successfully.")
    self.assertEqual(res.status_code, 201)

  def test_already_registered_user(self):
    """Test that a user cannit be registered twice."""
    res = self.client().post('/auth/register', data=self.user_data)
    self.assertEqual(res.status_code, 201)
    second_res = self.client().post('/auth/register', data=self.user_data)
    self.assertEqual(second_res.status_code, 202)
    result = json.loads(second_res.data.decode())
    self.assertEqual(
      result['message', "User already exists. please login"]
    )



