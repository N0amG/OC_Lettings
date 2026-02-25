"""Tests for the profiles application.

Covers models, views and URL resolution.
"""
import pytest
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse, resolve

from profiles.models import Profile
from profiles.views import profiles_index, profile


@pytest.fixture
def user(db):
    """Create and return a sample Django User instance."""
    return User.objects.create_user(
        username='testuser',
        first_name='John',
        last_name='Doe',
        email='john@example.com',
        password='password123',
    )


@pytest.fixture
def sample_profile(user):
    """Create and return a sample Profile instance."""
    return Profile.objects.create(user=user, favorite_city='Paris')


# --- Model tests ---

class TestProfileModel:
    """Unit tests for the Profile model."""

    def test_str(self, sample_profile):
        """Profile __str__ returns the associated username."""
        assert str(sample_profile) == 'testuser'


# --- URL tests ---

class TestProfilesUrls:
    """Integration tests for profiles URL resolution."""

    def test_profiles_index_url_resolves(self):
        """URL /profiles/ resolves to profiles_index view."""
        url = reverse('profiles:profiles_index')
        assert resolve(url).func == profiles_index

    def test_profile_detail_url_resolves(self):
        """URL /profiles/<username>/ resolves to profile view."""
        url = reverse('profiles:profile', kwargs={'username': 'testuser'})
        assert resolve(url).func == profile


# --- View tests ---

class TestProfilesViews:
    """Integration tests for profiles views."""

    def test_profiles_index_returns_200(self, db):
        """GET /profiles/ returns HTTP 200."""
        client = Client()
        url = reverse('profiles:profiles_index')
        response = client.get(url)
        assert response.status_code == 200

    def test_profiles_index_uses_correct_template(self, db):
        """GET /profiles/ uses profiles/profiles_index.html template."""
        client = Client()
        url = reverse('profiles:profiles_index')
        response = client.get(url)
        assert 'profiles/profiles_index.html' in [t.name for t in response.templates]

    def test_profile_detail_returns_200(self, sample_profile):
        """GET /profiles/<username>/ returns HTTP 200."""
        client = Client()
        url = reverse('profiles:profile', kwargs={'username': sample_profile.user.username})
        response = client.get(url)
        assert response.status_code == 200

    def test_profile_detail_uses_correct_template(self, sample_profile):
        """GET /profiles/<username>/ uses profiles/profile.html template."""
        client = Client()
        url = reverse('profiles:profile', kwargs={'username': sample_profile.user.username})
        response = client.get(url)
        assert 'profiles/profile.html' in [t.name for t in response.templates]

    def test_profile_detail_contains_username(self, sample_profile):
        """GET /profiles/<username>/ response contains the username."""
        client = Client()
        url = reverse('profiles:profile', kwargs={'username': sample_profile.user.username})
        response = client.get(url)
        assert b'testuser' in response.content
