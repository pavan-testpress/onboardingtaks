from django.conf.urls import url
from django.urls import path
from placesapp import views

app_name = "placesapp"
urlpatterns = [
    path('',views.List_View.as_view(),name="list"), 
    url(r'(?P<pk>\d+)$',views.Detail_View.as_view(),name="details"),
    path('<city>',views.List_View.as_view(),name="list"), 
    url(r'create/$',views.Create_View.as_view(),name="create"),
]