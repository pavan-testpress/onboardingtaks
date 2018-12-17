from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from invitationapp.models import Invitations

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.username = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class InvitationForm(forms.ModelForm):
    class Meta:
        model = Invitations
        fields = ['invitee_email',]
