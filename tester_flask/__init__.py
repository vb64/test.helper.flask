"""Test helper for Flask app.

http://flask.pocoo.org/docs/1.0/testing/
https://cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env
"""
import unittest
try:  # pragma: no cover
    from urllib import urlencode
    from urlparse import urlparse
except ImportError:  # pragma: no cover
    from urllib.parse import urlparse, urlencode  # pylint: disable=ungrouped-imports


class RequestFactory:  # pylint: disable=too-few-public-methods
    """Generator of the requests."""

    def __init__(self, app):
        """Save Flask app instance."""
        self.app = app

    def post(self, url, data='', content_type='application/octet-stream'):
        """Post requests tests."""
        return self.app.test_request_context(url, data=data, method='POST', content_type=content_type)


class TestFlask(unittest.TestCase):
    """Flask apps tester."""

    app = None
    client = None
    factory = None

    def set_up(self, app):
        """Set defaults for Flask testing."""
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.factory = RequestFactory(self.app)

    def get_url(self, view_name, **kwargs):
        """Generate url for view in app test context."""
        with self.app.test_request_context():
            from flask import url_for
            url = url_for(view_name, **kwargs)

        return url

    def guest_view(self, url, return_code=200, follow_redirects=False):
        """Generic get request."""
        response = self.client.get(url, follow_redirects=follow_redirects)

        assert response.status_code == return_code, "guest_view {}: {} -> {}".format(
          return_code, url, response.status_code
        )
        return response

    def simple_view(self, view_name, return_code=200, follow=False, get_param=None):
        """Simple get request."""
        url = self.get_url(view_name)
        if get_param:
            url = url + "?" + urlencode(get_param)
        return self.guest_view(url, return_code=return_code, follow_redirects=follow)

    def param_view(
      self, view_name, params, return_code=200, follow=False, get_param=None
    ):  # pylint: disable=too-many-arguments
        """Get request with parameters."""
        url = self.get_url(view_name, **params)
        if get_param:
            url = url + "?" + urlencode(get_param)
        return self.guest_view(url, return_code=return_code, follow_redirects=follow)

    def simple_post(self, view_name, post_dict, follow=True, content_type=None):
        """Simple post request."""
        url = self.get_url(view_name)
        return self.client.post(url, data=post_dict, follow_redirects=follow, content_type=content_type)

    def param_post(
      self, view_name, params, post_dict, follow=True, get_param=None, content_type=None
    ):  # pylint: disable=too-many-arguments
        """Post request with parameters."""
        url = self.get_url(view_name, **params)
        if get_param:
            url = url + "?" + urlencode(get_param)
        return self.client.post(url, data=post_dict, follow_redirects=follow, content_type=content_type)

    @staticmethod
    def final_url(response):
        """Return final url after redirect."""
        assert response.status_code == 302
        return urlparse(response.location).path
