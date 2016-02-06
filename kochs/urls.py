"""kochs URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from tentacles import views

urlpatterns = [
    url(r'^reports/institution/(?P<id>\d+)$', views.InstitutionReport),
    url(r'^reports/institution_full/(?P<id>\d+)$', views.InstitutionDonorsAndPeopleByYear),
    url(r'^d3', views.d3),
    url(r'^table/(?P<table_name>.+)$', views.Table),
    url(r'^api/people$', views.ListPeople.as_view()),
    url(r'^api/institutions', views.ListInstitutions.as_view()),
    url(r'^api/affiliations', views.ListAffiliations.as_view()),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls))
]
