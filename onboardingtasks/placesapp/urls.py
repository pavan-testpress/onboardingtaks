from django.conf.urls import url
from placesapp import views

app_name = "placesapp"
urlpatterns = [
    url(r'^$',views.List_View.as_view(),name="list"),
    url(r'(?P<pk>\d+)$',views.Detail_View.as_view(),name="details"),
    url(r'create/$',views.Create_View.as_view(),name="create"),
]