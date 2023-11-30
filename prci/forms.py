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
    publisher_founding_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        }),
    )


    is_publisher = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        }),
        label="Publisher",
    )

    # pub_founding_date = forms.DateField(
    #     widget=forms.DateInput(attrs={
    #         'class': 'form-control',
    #         'type': "date"
    #     }),
    # ),
