"""Models for the profiles application.

Defines the Profile model used to store additional user information.
"""
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Extends the default Django User with a favorite city field."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """Return the username as string representation."""
        return self.user.username
