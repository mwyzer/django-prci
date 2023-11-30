from django import forms
from .models import Publisher


class PublisherForm(forms.Form):
    pub_name = forms.CharField(
        max_length=50,
        label="Publisher Name",
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        }),
     
        help_text="Please enter your full name (first name and last name)"
    )
    pub_address = forms.CharField(
          max_length=50,
        label="Publisher Address",
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        }),
    )
    is_published = forms.BooleanField(
        label="Publisher"
    )
