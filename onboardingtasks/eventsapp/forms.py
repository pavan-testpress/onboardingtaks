from django.forms import ModelForm
from eventsapp.models import Events,EventTime
from django.contrib.admin import widgets 


class EventForm(ModelForm):
    class Meta:
        model = Events
        fields = "__all__"
class EventTimeForm(ModelForm):
    class Meta:
        model = EventTime
        fields = "__all__"
        widgets = {'event_start_time': widgets.AdminSplitDateTime(),'event_end_time': widgets.AdminSplitDateTime()}
