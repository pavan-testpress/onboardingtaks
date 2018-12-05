from django.urls import path
from django.conf.urls import url
from .views import HomePageView,NavPageView
from pagesapp.models import Pages

app_name="pagesapp"

urlpatterns = [
    path('',HomePageView.as_view(),name="home"),
    url (r'^',NavPageView.as_view())
]

