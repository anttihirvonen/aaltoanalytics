from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('aaltoanalytics.apps.analytics.views',
    url(r'^log/', 'log_pageview', name="analytics-log_pageview"),
    url(r'^test/', direct_to_template, {'template' : 'analytics/test.html' }, name="analytics-test"),
    url(r'^show/', 'show_raw_log', name="analytics-show"),
)
