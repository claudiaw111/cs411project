"""levelup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
#from app.views import test

urlpatterns = patterns('',
    url(r'^$', 'app.views.home', name = 'home'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^create/$', 'app.views.createUser', name = 'create'),
    url(r'^home/$', 'app.views.home', name = 'home'),

    #url(r'^auth/$', 'app.views.auth'),
    #url(r'^auth/$', 'app.views.auth_view', name='auth'),
    url(r'^login/$', 'app.views.user_login', name = 'login'),
    url(r'^auth/$', 'app.views.auth_view', name='auth'),
    url(r'^invalid/$', 'app.views.invalid_login', name='invalid_login'),
    url(r'^logout/$', 'app.views.logout_view', name = 'logout'),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^fitbit/', include('fitapp.urls')),
    url(r'^test/$', 'app.views.test', name = 'test'),
    url(r'^register/$', 'app.views.register_user', name = 'register'),
    url(r'^register_success/$', 'app.views.register_success', name = 'success'),
    url(r'^createGroup/$', 'app.views.createGroup', name = 'createGroup'),
    url(r'^createGroup_success/$', 'app.views.createGroup_success', name = 'createGroup_success'),
    url(r'^createGroup_invalid/$', 'app.views.createGroup_invalid', name = 'createGroup_invalid'),
    url(r'^createChallenge/$', 'app.views.createChallenge', name = 'createChallenge'),
    url(r'^createChallenge_success/$', 'app.views.createChallenge_success', name='createChallenge_success'),
    url(r'^createChallenge_invalid/$', 'app.views.createChallenge_invalid', name='createChallenge_invalid'),
    url(r'^joinGroup/$', 'app.views.joinGroup', name='joinGroup'),
    url(r'^joinInvalid/$', 'app.views.join_invalid', name='joinInvalid'),
    url(r'^join_success/$', 'app.views.join_success', name='join_success'),
    url(r'^group/$', 'app.views.group_pg', name='group'),
    url(r'^challenge/$', 'app.views.challenge_pg', name='challenge'),
    url(r'^user/$', 'app.views.user_pg', name='user'),
)
