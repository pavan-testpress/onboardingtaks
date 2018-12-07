from django.shortcuts import render
from django.views.generic import ListView,CreateView
from eventsapp.models import Events,EventTime
from eventsapp.forms import EventForm,EventTimeForm
# Create your views here.

class EventsListView(ListView):
    model = Events
    template_name = "eventsapp/base.html"

class EventsCreateView(CreateView):
    def get(self,request):
        eform = EventForm()
        tform = EventTimeForm()
        template_name = "eventsapp/createview.html"
        return render(request,template_name,{'eform':eform,'tform':tform,}) 