from django import forms
from .models import Publisher


class PublisherForm(forms.Form):
    pub_name = forms.CharField()
    pub_address = forms.CharField()
