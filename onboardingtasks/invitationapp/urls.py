from django.urls import path
from invitationapp import views


app_name = 'invitationapp'

urlpatterns = [
    path('',views.login,name='login')
]
