from django.urls import path
from . import views

urlpatterns = [
    path('create', views.CreateUserAccounts.as_view(), name="create"),
]
