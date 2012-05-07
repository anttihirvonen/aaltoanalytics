# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('aaltoanalytics.apps.analytics.views',
    url(r'^log/$', 'log_pageview', name="analytics-log_pageview"),
    url(r'^log/updatetime/(?P<pageview_id>\d+)/$', 'update_last_read_time', name="analytics-update_time"),
    url(r'^test/', direct_to_template, {'template' : 'analytics/test.html' }, name="analytics-test"),
)
