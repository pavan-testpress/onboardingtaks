from django.urls import path
from invitationapp import views


app_name = 'invitationapp'

urlpatterns = [
    path('',views.index,name="index"),
    path('login/',views.login,name='login'),
    path('signup/',views.singup,name='signup'),
    path('logout/',views.logout,name='logout'),
]
