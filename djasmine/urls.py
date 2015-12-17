# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<spec>[\w/-]+\.[Ss]pec\.js)?/?$',
        views.jasmine_run_spec,
        name='jasmine-run-spec'),
]
