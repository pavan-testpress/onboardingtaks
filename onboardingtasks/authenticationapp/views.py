from django.contrib.auth import authenticate, login as mylogin, logout as mylogout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import UserCreationForm
from django.core.mail import send_mail
from invitationapp.models import Invitations

# Create your views here.


def index(request):
    if str(request.user) == 'AnonymousUser':
        return HttpResponseRedirect(reverse('authenticationapp:login'))
    else:
        return render(request, 'authenticationapp/index.html')


def login(request):
    if request.method == 'GET':
        template = 'authenticationapp/login.html'
        return render(request, template)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            mylogin(request, user)
            return HttpResponseRedirect(reverse('authenticationapp:index'))
        else:
            return render(request, "authenticationapp/invalidlogin.html")


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            data_from_table = form.save()
            invitor_exist = Invitations.objects.filter(invitee_email=data_from_table.email, registered='False')
            if invitor_exist:
                for i in invitor_exist:
                    i.registered = 'True'
                    i.save()
                    print(str(i.invitee_email), str(i.invitor_email))
                    send_mail('Invitaion', str(i.invitee_email) + ' has accepted your invitation and registered',
                              'pavan1995143.pavan@gmail.com', [str(i.invitor_email), ])

            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=raw_password)
            mylogin(request, user)
            return HttpResponseRedirect(reverse('authenticationapp:index'))
    else:
        form = UserCreationForm()
    return render(request, 'authenticationapp/signup.html', {'form': form})


def logout(request):
    mylogout(request)
    return HttpResponseRedirect(reverse('authenticationapp:login'))
