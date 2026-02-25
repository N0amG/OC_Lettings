"""Views for the oc_lettings_site application.

Handles the home page and custom HTTP error pages.
"""
from django.shortcuts import render


def index(request):
    """Render the home page."""
    return render(request, 'index.html')


def handler404(request, exception):
    """Render the custom 404 error page."""
    return render(request, '404.html', status=404)


def handler500(request):
    """Render the custom 500 error page."""
    return render(request, '500.html', status=500)
