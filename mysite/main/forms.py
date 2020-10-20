from django import forms
from django.conf import settings
import requests


class BreedSelectionForm(forms.Form):
    breed_selection = forms.CharField(max_length=100)

    def search(self):
        result = {}
        breed_selection = self.cleaned_data['breed_selection']
        endpoint = 'https://dog.ceo/api/breed/{breed}/images'
        url = endpoint.format(breed=breed_selection)
        response = requests.get(url)
        if response.status_code == 200:
            result = response.json()
            result['success'] = True
        else:
            result['success'] = False
            if response.status_code == 404:
                result['message'] = 'No entries found for "%s"' % breed_selection
            else:
                result['message'] = 'Dog API is not available at the moment'
        return result
