from django import forms
from .models import Pages


class PagesForm(forms.ModelForm):
    class Meta:
        model = Pages
        exclude = ('slug',)
