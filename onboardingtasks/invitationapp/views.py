from django.shortcuts import render
from .forms import InvitationForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Invitations
from django.contrib.auth.models import User
from django.core.mail import send_mail


# Create your views here.


def index(request):
    if request.user.is_authenticated:
        invite_list = Invitations.objects.filter(user=request.user)
        if request.method == "GET":
            form = InvitationForm()
            return render(request, "invitationapp/index.html", {'form': form, 'invite_list': invite_list})
        if request.method == "POST":
            form = InvitationForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.invitor_email = request.user.email
                form.user = User.objects.get(username=request.user)
                form.save()
                send_mail('Invitaion', str(
                    request.user) + ' invited you to register the app: http://127.0.0.1:8000/invitations/signup/ ',
                          'pavan1995143.pavan@gmail.com', [form.invitee_email, ])
                send_mail('Invitaion', 'Invition has been sent to ' + form.invitee_email,
                          'pavan1995143.pavan@gmail.com', [form.invitor_email, ])
            return HttpResponseRedirect(reverse('invitationapp:index'))
    else:
        return HttpResponseRedirect(reverse('authenticationapp:login'))
