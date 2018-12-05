from django import forms 
from pagesapp.models import Pages

class PagesForm(forms.ModelForm):
    class Meta:
        model = Pages
        exclude = ('slug',)