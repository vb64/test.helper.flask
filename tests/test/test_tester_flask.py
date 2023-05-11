"""Package tester_flask.

make test T=test_tester_flask
"""
from tester_flask import TestFlask
from tests.flask_app import app


class TestSetup(TestFlask):
    """Test SetUp method."""

    def setUp(self):
        """Init with flask app."""
        super(TestSetup, self).setUp()
        TestFlask.set_up(self, app)

    def test_default(self):
        """Check defaults."""
        assert self.client
        assert self.factory

    def test_simple_view(self):
        """Check simple_view."""
        assert self.simple_view('main_page').status_code == 200
        assert self.simple_view('main_page', get_param={'hello': 1}).status_code == 200

    def test_param_view(self):
        """Check param_view."""
        assert self.param_view('main_page', {'one': 1}).status_code == 200
        assert self.param_view('main_page', {'one': 1}, get_param={'hello': 1}).status_code == 200

    def test_simple_post(self):
        """Check simple_post."""
        assert self.simple_post('main_page', {'one': 1}).status_code == 200

    def test_param_post(self):
        """Check param_post."""
        assert self.param_post('main_page', {'hello': 1}, {'one': 1}).status_code == 200
        assert self.param_post('main_page', {'hello': 1}, {'one': 1}, get_param={'hi': 1}).status_code == 200

    def test_redirect(self):
        """Check redirect."""
        response = self.simple_post('redirect_page', {'one': 1}, follow=False)
        assert self.final_url(response) == self.get_url('main_page')

    def test_factory(self):
        """Check factory."""
        response = self.factory.post(self.get_url('redirect_page'))
        assert response
