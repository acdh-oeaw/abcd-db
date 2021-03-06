from django.conf.urls import url
from django.views.generic.base import RedirectView
from . import views
from archiv import search_result_views
from django_spaghetti.views import Plate
app_name = 'webpage'

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    url(r'^favicon\.ico$', favicon_view),
    url(r'^imprint', views.ImprintView.as_view(), name="imprint"),
    url(
        r'^data-model',
        Plate.as_view(
            plate_template_name="webpage/data_model.html"
        ),
        name="data_model"
    ),
    url(r'^$', views.GenericWebpageView.as_view(), name="start"),
    url(r'^results', search_result_views.EventResultView.as_view(), name="results"),
    url(r'^accounts/login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'^project-info/$', views.project_info, name='project_info'),
    url(r'^(?P<template>[\w-]+)/$', views.GenericWebpageView.as_view(), name='staticpage'),
]
