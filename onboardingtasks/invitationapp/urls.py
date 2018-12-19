from django.urls import path
from . import views


app_name = 'invitationapp'

urlpatterns = [
    path('', views.index, name="index"),
]
