from django.urls import path
from .views import HomeView, signup

app_name = 'home'
urlpatterns = [
    path('signup', signup, name="signup"),
    path('', HomeView.as_view(), name='index'),
    path('add', HomeView.as_view()),
    path('post', HomeView.as_view()),
    path('get', HomeView.as_view()),
    path('folder', HomeView.as_view()),
    
]
