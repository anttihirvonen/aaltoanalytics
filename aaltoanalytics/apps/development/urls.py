# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('aaltoanalytics.apps.development.views',
    url(r'^$', 'development_index', name="development-index"),
    url(r'show/$', 'development_show_raw_log', name="development-show"),
)
