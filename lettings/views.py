"""Views for the lettings application.

Handles rendering of the lettings list and individual letting detail pages.
"""
from django.shortcuts import render
from .models import Letting


def lettings_index(request):
    """Render the list of all available lettings."""
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/lettings_index.html', context)


def letting(request, letting_id):
    """Render the detail page for a specific letting identified by its ID."""
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
