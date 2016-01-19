"""translator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^index', views.index),
    url(r'^register/(?P<jobcode>[a-z]+)', views.register),
    url(r'^manage/unassigned', views.unassigned),
    url(r'^manage/assign/(?P<article_id>\d+)', views.assign_translator),
    url(r'^manage/assigned/(?P<article_id>\d+)/(?P<translator_id>\d+)', views.assigned),
    url(r'^wordcount', views.wordcount),
    url(r'^create', views.create_article),
    url(r'^confirm_article', views.confirm_article),
    url(r'^confirm_yes', views.confirm_yes),
    url(r'^confirm_no', views.confirm_no),
    url(r'^untranslated', views.untranslated),
    url(r'^translate/(?P<article_id>\d+)', views.translate),
    url(r'^auth', views.auth_view),
    url(r'^login', views.login),
    url(r'^logout', views.logout),
    url(r'^loggedin', views.loggedin),
    url(r'^translator_dashboard', views.translator_dashboard),
    url(r'^client_dashboard', views.client_dashboard)
]
