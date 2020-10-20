from django.shortcuts import render
from .forms import BreedSelectionForm
import requests

# Create your views here.


def homepage(request):
    search_result = {}
    if 'breed_selection' in request.GET:
        breed_selection_form = BreedSelectionForm(request.GET)
        if breed_selection_form.is_valid():
            search_result = breed_selection_form.search()
    else:
        breed_selection_form = BreedSelectionForm()

    return render(request=request,
                  template_name='main/home.html',
                  context={'breed_selection_form': breed_selection_form, 'search_result': search_result})
