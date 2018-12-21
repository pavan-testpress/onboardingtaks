from django.views.generic import CreateView, ListView, DetailView
from .models import Places
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
        if 'city' in self.kwargs:
            qs = qs.filter(city__iexact=self.kwargs['city'])
        return qs


class Create_View(CreateView):
    model = Places
    fields = '__all__'

    def get_success_url(self):
        url = self.request.GET['path']
        return url
