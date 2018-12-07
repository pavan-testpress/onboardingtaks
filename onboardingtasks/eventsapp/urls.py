from django.urls import path
from eventsapp import views


app_name = "eventsapp"
urlpatterns = [
    path('',views.EventsListView.as_view(),name="list"),
    path('create',views.EventsCreateView.as_view(),name='create'),
]
