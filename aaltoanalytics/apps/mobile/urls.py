# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('aaltoanalytics.apps.mobile.views',
    url(r'^$', 'mobile_index', name="mobile-index"),
    url(r'^content/hot/$', 'mobile_hot_content', name="mobile-hot_content"),
    url(r'^content/mostviewed/$', 'mobile_most_viewed_content', name="mobile-most_viewed_content"),
    url(r'^users/activeperservice/$', 'mobile_active_users_per_service', name="mobile-active_users_per_service"),
)
