"""onboardingtasks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
<<<<<<< 7ffb166401fd1d983a7a9e87056ef94dc878337f
from django.conf.urls import url
=======
>>>>>>>  added root page,bootstrap to all apps and some enhancments to placesapp filter and for signin sessions
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('pages/', include('pagesapp.urls')),
    path('bookmarks/', include('bookmarksapp.urls')),
    path('admin/', admin.site.urls),
<<<<<<< 7ffb166401fd1d983a7a9e87056ef94dc878337f
    path('bookmarks/', include('django.contrib.auth.urls')),
    url(r'^places/', include('placesapp.urls')),
=======
    path('places/', include('placesapp.urls')),
>>>>>>>  added root page,bootstrap to all apps and some enhancments to placesapp filter and for signin sessions
    path('events/', include('eventsapp.urls')),
    path('invitations/', include('invitationapp.urls')),
]
