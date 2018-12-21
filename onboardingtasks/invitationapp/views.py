from django.shortcuts import render
from django.contrib.auth import login as mylogin , authenticate, logout as mylogout
from .forms import UserCreationForm, InvitationForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Invitations
from django.contrib.auth.models import User
from django.core.mail import send_mail

# Create your views here.


def login(request):
    if request.method == 'GET':
        template = 'invitationapp/login.html'
        return render(request, template)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            mylogin(request, user)
            return HttpResponseRedirect(reverse('invitationapp:index'))
                
        else:
            # Return an 'invalid login' error message.
            return render(request, "invitationapp/invalidlogin.html")


def singup(request):
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
            user = authenticate(username=username, password=raw_password)
            mylogin(request, user)
            return HttpResponseRedirect(reverse('invitationapp:index'))
    else:
        form = UserCreationForm()
    return render(request, 'invitationapp/signup.html', {'form': form})


def logout(request):
    mylogout(request)
    return HttpResponseRedirect(reverse('invitationapp:login'))


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
                send_mail('Invitaion', str(request.user) +
                          ' invited you to register the app: http://127.0.0.1:8000/invitations/signup/ ',
                          'pavan1995143.pavan@gmail.com', [form.invitee_email, ])
                send_mail('Invitaion', 'Invition has been sent to '+form.invitee_email,
                          'pavan1995143.pavan@gmail.com', [form.invitor_email, ])
            return HttpResponseRedirect(reverse('invitationapp:index')) 
    else:
        return HttpResponseRedirect(reverse('invitationapp:login'))
