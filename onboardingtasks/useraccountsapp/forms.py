from django import forms
from .models import UserAccounts


class CreateUserAccountsForm(forms.ModelForm):
    class Meta:
        model = UserAccounts
        fields = '__all__'
        widgets = {
            'gender': forms.RadioSelect(),
            'date_of_birth': forms.DateInput(attrs={'placeholder': 'DD-MM-YYYY', 'format': '%d-%m-%Y'})
        }
