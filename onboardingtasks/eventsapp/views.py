from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Events, EventTime
from .forms import EventForm, EventTimeForm
from datetime import datetime
# Create your views here.


class EventsListView(ListView):
    model = Events
    template_name = "eventsapp/list.html"

    def get(self, request):
        events = self.get_queryset(request)
        return render(request, self.template_name, {'events': events})

    def get_queryset(self, request):
        qs = super().get_queryset()
        results = set()
        if 'weekday' in request.GET:
            for q in qs:
                c_all = q.event_times.all()
                for c in c_all:
                    if str(c.event_start_time.weekday()) == (request.GET['weekday']):
                        results.add(q)
            return results
        elif'yyyy-mm' in request.GET:
            year, month = request.GET['yyyy-mm'].split('-')
            qs = set(qs.filter(event_times__event_start_time__year=year, event_times__event_start_time__month=month))
        elif 'yyyy-mm-dd' in request.GET:
            year, month, date = request.GET['yyyy-mm-dd'].split('-')
            qs = set(qs.filter(event_times__event_start_time__year=year, event_times__event_start_time__month=month, event_times__event_start_time__day=date))
        return qs


class EventsCreateView(CreateView):
    def get(self, request):
        eform = EventForm()
        tform = EventTimeForm()
        template_name = "eventsapp/createview.html"
        return render(request, template_name, {'eform': eform, 'tform': tform, })

    def post(self, request):
        template_name = "eventsapp/createview.html"
        eform = EventForm(request.POST)
        if eform.is_valid():
            eform.title = eform.cleaned_data['title']
            eform.place = eform.cleaned_data['place']
            eform.tags = eform.cleaned_data['tags']
            eform.created_by = eform.cleaned_data['created_by']
            e = eform.save()
        tform = EventTime()
        event_start_time = request.POST['event_start_time_0'] + " " + request.POST['event_start_time_1']
        event_start_time = datetime.strptime(event_start_time, '%Y-%m-%d %H:%M:%S')
        tform.event_start_time = event_start_time
        event_end_time = request.POST['event_end_time_0'] + " " + request.POST['event_end_time_1']
        event_end_time = datetime.strptime(event_end_time, '%Y-%m-%d %H:%M:%S')
        tform.event_end_time = event_end_time
        tform.event = Events.objects.get(pk=e.pk)
        tform.save()
        return render(request, template_name, {})
