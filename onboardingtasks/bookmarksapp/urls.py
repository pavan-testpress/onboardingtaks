from django.urls import path
<<<<<<< 7ffb166401fd1d983a7a9e87056ef94dc878337f
from .views import HomeView, signup

app_name ='home'
urlpatterns = [
    path('signup', signup, name="signup"),
    path('', HomeView.as_view()),
    path('add', HomeView.as_view()),
    path('post', HomeView.as_view()),
    path('get', HomeView.as_view()),
    path('folder', HomeView.as_view()),
    
]
=======
from . import views

app_name = 'bookmarksapp'
urlpatterns = [
    path('', views.HomeView.as_view(), name="index"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
>>>>>>>  added root page,bootstrap to all apps and some enhancments to placesapp filter and for signin sessions
