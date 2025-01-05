
from django import forms
from datetime import timedelta
from django.utils import timezone

class URLSubmitForm(forms.Form):
    url = forms.URLField(
        label='Long URL',
        widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter your URL here'})
    )
    expiration_days = forms.IntegerField(
        label='Expiration (days)',
        required=False,
        min_value=1,
        max_value=365,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Optional: Days until expiration'})
    )

class URLLookupForm(forms.Form):
    short_code = forms.CharField(
        label='Short Code',
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter short code'})
    )