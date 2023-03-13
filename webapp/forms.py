from django import forms
from .models import Searchs

class SearchForm(forms.ModelForm):
    address = forms.CharField(label='')
    class Meta:
        model = Searchs
        fields =['address',]

