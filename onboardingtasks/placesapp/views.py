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
    template_name = 'placesapp/listplaces.html'

    def get_queryset(self):
        qs = super(List_View, self).get_queryset()
        #print(self.request.GET)
        if 'city' not in self.request.GET or self.request.GET['city'] == "All":
            qs = super(List_View, self).get_queryset()
        else:
            qs = qs.filter(city__iexact=self.request.GET['city'])
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'city' not in self.request.GET or self.request.GET['city'] == "All":
            context['city'] = 'All'
        else:
            context['city'] = self.request.GET['city']
        return context

class Create_View(CreateView):
    model = Places
    fields = '__all__'
    def get_success_url(self):
        url = self.request.GET['path']
        return url
