from django.shortcuts import render
from django.views.generic import CreateView,ListView,DetailView
from placesapp.models import Places
# Create your views here.

class Detail_View(DetailView):
    context_object_name = "place"
    model = Places
    template_name = 'placesapp/placedetails.html'

class List_View(ListView):
    context_object_name = "places"
    model = Places
    list_filter = ['city',]
    template_name = 'placesapp/listplaces.html'

class Create_View(CreateView):
    model = Places
    fields = '__all__'
