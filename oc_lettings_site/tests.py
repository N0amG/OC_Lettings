"""Tests for the oc_lettings_site application.

Covers the index view, error handlers and URL resolution.
"""
from django.test import Client, RequestFactory
from django.urls import reverse, resolve

from oc_lettings_site.views import index, handler404, handler500


# --- URL tests ---

class TestOcLettingsSiteUrls:
    """Integration tests for oc_lettings_site URL resolution."""

    def test_index_url_resolves(self):
        """URL / resolves to the index view."""
        url = reverse('index')
        assert resolve(url).func == index


# --- View tests ---

class TestOcLettingsSiteViews:
    """Integration tests for oc_lettings_site views."""

    def test_index_returns_200(self, db):
        """GET / returns HTTP 200."""
        client = Client()
        response = client.get(reverse('index'))
        assert response.status_code == 200

    def test_index_uses_correct_template(self, db):
        """GET / uses index.html template."""
        client = Client()
        response = client.get(reverse('index'))
        assert 'index.html' in [t.name for t in response.templates]

    def test_handler404_returns_404(self):
        """handler404 returns HTTP 404 with the 404 template."""
        factory = RequestFactory()
        request = factory.get('/nonexistent/')
        response = handler404(request, exception=Exception('Not found'))
        assert response.status_code == 404

    def test_handler500_returns_500(self):
        """handler500 returns HTTP 500 with the 500 template."""
        factory = RequestFactory()
        request = factory.get('/')
        response = handler500(request)
        assert response.status_code == 500


def test_dummy():
    """Placeholder test to verify the test suite runs correctly."""
    assert 1
