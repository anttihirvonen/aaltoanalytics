# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('aaltoanalytics.apps.mobile.views',
    url(r'^$', 'mobile_index', name="analytics-mobile_index"),
    url(r'^content/hot/$', 'mobile_hot_content', name="analytics-mobile_hot_content"),
    url(r'^content/mostviewed/$', 'mobile_most_viewed_content', name="analytics-mobile_most_viewed_content"),
    url(r'^users/activeperservice/$', 'mobile_active_users_per_service', name="analytics-mobile_active_users_per_service"),
)
