"""Tests for the lettings application.

Covers models, views and URL resolution.
"""
import pytest
from django.test import Client
from django.urls import reverse, resolve

from lettings.models import Address, Letting
from lettings.views import index, letting


@pytest.fixture
def address(db):
    """Create and return a sample Address instance."""
    return Address.objects.create(
        number=10,
        street='Downing Street',
        city='London',
        state='LO',
        zip_code=75000,
        country_iso_code='GBR',
    )


@pytest.fixture
def sample_letting(address):
    """Create and return a sample Letting instance."""
    return Letting.objects.create(title='10 Downing Street', address=address)


# --- Model tests ---

class TestAddressModel:
    """Unit tests for the Address model."""

    def test_str(self, address):
        """Address __str__ returns number and street."""
        assert str(address) == '10 Downing Street'


class TestLettingModel:
    """Unit tests for the Letting model."""

    def test_str(self, sample_letting):
        """Letting __str__ returns its title."""
        assert str(sample_letting) == '10 Downing Street'


# --- URL tests ---

class TestLettingsUrls:
    """Integration tests for lettings URL resolution."""

    def test_lettings_index_url_resolves(self):
        """URL /lettings/ resolves to index view."""
        url = reverse('lettings:index')
        assert resolve(url).func == index

    def test_letting_detail_url_resolves(self):
        """URL /lettings/<id>/ resolves to letting view."""
        url = reverse('lettings:letting', kwargs={'letting_id': 1})
        assert resolve(url).func == letting


# --- View tests ---

class TestLettingsViews:
    """Integration tests for lettings views."""

    def test_lettings_index_returns_200(self, db):
        """GET /lettings/ returns HTTP 200."""
        client = Client()
        url = reverse('lettings:index')
        response = client.get(url)
        assert response.status_code == 200

    def test_lettings_index_uses_correct_template(self, db):
        """GET /lettings/ uses lettings/index.html template."""
        client = Client()
        url = reverse('lettings:index')
        response = client.get(url)
        assert 'lettings/index.html' in [t.name for t in response.templates]

    def test_letting_detail_returns_200(self, sample_letting):
        """GET /lettings/<id>/ returns HTTP 200."""
        client = Client()
        url = reverse('lettings:letting', kwargs={'letting_id': sample_letting.id})
        response = client.get(url)
        assert response.status_code == 200

    def test_letting_detail_uses_correct_template(self, sample_letting):
        """GET /lettings/<id>/ uses lettings/letting.html template."""
        client = Client()
        url = reverse('lettings:letting', kwargs={'letting_id': sample_letting.id})
        response = client.get(url)
        assert 'lettings/letting.html' in [t.name for t in response.templates]

    def test_letting_detail_contains_title(self, sample_letting):
        """GET /lettings/<id>/ response contains the letting title."""
        client = Client()
        url = reverse('lettings:letting', kwargs={'letting_id': sample_letting.id})
        response = client.get(url)
        assert b'10 Downing Street' in response.content
