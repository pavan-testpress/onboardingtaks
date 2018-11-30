from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .models import Bookmarks
# Create your views here.

class HomeView(TemplateView):
    template_name = "bookmarksapp/index.html"

    def get(self,request):
        bookmarks = Bookmarks.objects.all()
        return render(request,self.template_name,{'bookmarks':bookmarks})
    
    def post(self,request,bookmark_id):
        if 'edit' in request.POST:
            bookmark = Bookmarks.objects.get(pk=bookmark_id)
            bookmark.bookmark_url = request.POST['bookmark_url']
            bookmark.name = request.POST['name']
            bookmark.description = request.POST['description']
            bookmark.save()
        elif 'delete' in request.POST:
            bookmark = Bookmarks.objects.get(pk=bookmark_id)
            bookmark.delete()
        elif 'add' in request.POST:
            bookmark = Bookmarks()
            bookmark.bookmark_url = request.POST['bookmark_url']
            bookmark.name = request.POST['name']
            bookmark.description = request.POST['description']
            bookmark.save()
        return redirect('/bookmarks/')