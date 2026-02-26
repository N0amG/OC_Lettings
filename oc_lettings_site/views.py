"""Views for the oc_lettings_site application.

Handles the home page and custom HTTP error pages.
"""

import logging

from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    """Render the home page."""
    logger.info("Home page requested")
    return render(request, "index.html")


def handler404(request, exception):
    """Render the custom 404 error page."""
    logger.error("404 error: %s", request.path)
    return render(request, "404.html", status=404)


def handler500(request):
    """Render the custom 500 error page."""
    logger.error("500 error on: %s", request.path)
    return render(request, "500.html", status=500)


def trigger_error(request):
    """View to trigger a test error for Sentry integration testing."""
    return 1 / 0
