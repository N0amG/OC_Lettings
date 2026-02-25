"""Views for the profiles application.

Handles rendering of the profiles list and individual profile detail pages.
"""
from django.shortcuts import render
from .models import Profile


def index(request):
    """Render the list of all user profiles."""
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """Render the detail page for a specific profile identified by username."""
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
