from django.urls import path
from .views import HomeView 

appname ='home'
urlpatterns = [
    path('',HomeView.as_view(),name='index'),
    path('post/<int:bookmark_id>',HomeView.as_view(),name="index_post"),
    path('post/addnew/<int:bookmark_id>',HomeView.as_view(),name='index_add'),
]