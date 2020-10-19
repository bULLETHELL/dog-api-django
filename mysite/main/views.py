from django.shortcuts import render
import requests

# Create your views here.


def homepage(request):
    breeds_response = requests.get('https://dog.ceo/api/breeds/list/all')
    breeds = breeds_response.json()

    breed_selection_response = requests.get(
        'https://dog.ceo/api/breed/hound/images')
    breed_selection = breed_selection_response.json()

    return render(request=request,
                  template_name='main/home.html',
                  context={'breeds': breeds['message'], 'breed_selection': breed_selection['message']})
