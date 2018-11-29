from django.shortcuts import render
from django.http import HttpResponse
from .models import Bookmarks
# Create your views here.

def index(request):
    bookmarks = Bookmarks.objects.all()
    return render(request,'bookmarksapp/index.html',{'bookmarks':bookmarks})