"""Views for the lettings application.

Handles rendering of the lettings list and individual letting detail pages.
"""
import logging

from django.shortcuts import render
from .models import Letting

logger = logging.getLogger(__name__)


def index(request):
    """Render the list of all available lettings."""
    logger.info("Lettings index requested")
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """Render the detail page for a specific letting identified by its ID."""
    logger.info("Letting detail requested: id=%s", letting_id)
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
