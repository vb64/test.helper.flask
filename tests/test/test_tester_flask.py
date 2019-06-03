"""
make test T=test_tester_flask
"""
import os
from tester_flask import TestFlask
from tests.flask_app import app


class TestSetup(TestFlask):
    """
    Test SetUp method
    """
    def setUp(self):
        TestFlask.setUp(self, app)

    def test_default(self):
        """
        defaults
        """
        self.assertTrue(self.client)
        self.assertTrue(self.factory)

    def test_simple_view(self):
        """
        simple_view
        """
        self.assertEqual(self.simple_view('main_page').status_code, 200)
        self.assertEqual(self.simple_view('main_page', get_param={'hello': 1}).status_code, 200)

    def test_param_view(self):
        """
        param_view
        """
        self.assertEqual(self.param_view('main_page', {'one': 1}).status_code, 200)
        self.assertEqual(self.param_view('main_page', {'one': 1}, get_param={'hello': 1}).status_code, 200)

    def test_simple_post(self):
        """
        simple_post
        """
        self.assertEqual(self.simple_post('main_page', {'one': 1}).status_code, 200)

    def test_param_post(self):
        """
        param_post
        """
        self.assertEqual(self.param_post('main_page', {'hello': 1}, {'one': 1}).status_code, 200)
        self.assertEqual(self.param_post('main_page', {'hello': 1}, {'one': 1}, get_param={'hi': 1}).status_code, 200)

    def test_redirect(self):
        """
        redirect
        """
        response = self.simple_post('redirect_page', {'one': 1}, follow=False)
        self.assertEqual(self.final_url(response), self.get_url('main_page'))

    def test_factory(self):
        """
        factory
        """
        response = self.factory.post(self.get_url('redirect_page'))
        self.assertTrue(response)
