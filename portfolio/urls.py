"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from main import views, serializers
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers, viewsets


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.Home.as_view(lang='en-us')),
    url(r'^pt-br/$', views.Home.as_view(lang='pt-br')),
    url(r'^contact/$', views.ContactView.as_view(lang="en-us"), name='contact'),
    url(r'^pt-br/contato/$', views.ContactView.as_view(lang="pt-br"), name='contato'),

    #REST
    url(r'^rest/$', views.api_root),
    url(r'^rest/user/$', views.UserList.as_view(), name='user-list'),
    url(r'^rest/user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^rest/person/$', views.PersonList.as_view(), name='person-list'),
    url(r'^rest/person/(?P<pk>[0-9]+)/$', views.PersonDetail.as_view(), name='person-detail'),
    url(r'^rest/contact/$', views.ContactList.as_view(), name='contact-list'),
    url(r'^rest/contact/(?P<pk>[0-9]+)/$', views.ContactDetail.as_view(), name='contact-detail'),
]
