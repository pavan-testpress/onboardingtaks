from django import forms
from .models import Invitations


class InvitationForm(forms.ModelForm):
    class Meta:
        model = Invitations
        fields = ['invitee_email',]
