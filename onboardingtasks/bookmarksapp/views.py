from django.contrib.auth import login as mylogin, authenticate, logout as mylogout
from .forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect,reverse
from django.views.generic import TemplateView
from .models import Bookmarks,Folders
# Create your views here.


def login(request):
    if request.method == 'GET':
        template = 'bookmarksapp/login.html'
        return render(request, template)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            mylogin(request, user)
            return HttpResponseRedirect(reverse('bookmarksapp:index'))

        else:
            # Return an 'invalid login' error message.
            return render(request, "bookmarksapp/invalidlogin.html")


def logout(request):
    mylogout(request)
    return HttpResponseRedirect(reverse('bookmarksapp:login'))


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            mylogin(request, user)
            return HttpResponseRedirect(reverse('bookmarksapp:index'))
    else:
        form = UserCreationForm()
    return render(request, 'bookmarksapp/signup.html', {'form': form})


class HomeView(TemplateView):
    template_name = "bookmarksapp/index.html"

    def get(self,request):
        if request.user.is_authenticated:
            if 'id' in request.GET and request.GET['id']!='1':
                bookmarks = Bookmarks.objects.filter(folder_name=  request.GET['id'],user=request.user)
            else:
                bookmarks = Bookmarks.objects.filter(user=request.user)
            folders = Folders.objects.filter(user=request.user)
            return render(request,self.template_name,{'bookmarks':bookmarks,'folders':folders})
        else:
            return HttpResponseRedirect(reverse('bookmarksapp:login'))
    def post(self,request):
        if 'edit' in request.POST:
            folder = Folders.objects.get(id=int(request.POST['folder_list']),user=request.user)
            bookmark = Bookmarks.objects.get(pk=int(request.POST['id']))
            bookmark.bookmark_url = request.POST['bookmark_url']
            bookmark.name = request.POST['name']
            bookmark.description = request.POST['description'].strip()
            bookmark.folder_name = folder
            bookmark.user=request.user
            bookmark.save()
        elif 'delete' in request.POST:
            bookmark = Bookmarks.objects.get(pk=int(request.POST['id']))
            bookmark.delete()
        elif 'add' in request.POST:
            bookmark = Bookmarks()
            folder = Folders.objects.get(id=int(request.POST['folder_list']),user=request.user)
            bookmark.bookmark_url = request.POST['bookmark_url']
            bookmark.name = request.POST['name']
            bookmark.description = request.POST['description'].strip()
            bookmark.folder_name = folder
            bookmark.user=request.user
            bookmark.save()
        elif 'add_folder' in request.POST:
            folder = Folders()
            folder.folder_name = request.POST['folder']
            folder.user=request.user
            folder.save()
        return redirect('/bookmarks/', request)


