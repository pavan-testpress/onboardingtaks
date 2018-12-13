from django.shortcuts import render
from django.contrib.auth import login as mylogin , authenticate

# Create your views here.
def login(request):
    if request.method == 'GET':
        template = 'invitationapp/login.html'
        return render(request,template)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            mylogin(request,user)
            print('Yes'+str(user))
            return render(request,"invitationapp/index.html")
                
        else:
            # Return an 'invalid login' error message.
            return render(request,"invitationapp/invalidlogin.html")