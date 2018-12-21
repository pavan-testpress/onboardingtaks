from django.urls import path
from . import views


app_name = 'invitationapp'

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name='login'),
    path('signup/', views.singup, name='signup'),
    path('logout/', views.logout, name='logout'),
]
