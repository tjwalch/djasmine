# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<spec>[\w-]+\.spec\.js)/$',
        views.jasmine_run_one_spec,
        name='jasmine-run-one-spec'),
]
