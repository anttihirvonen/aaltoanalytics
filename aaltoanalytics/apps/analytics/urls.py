from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('aaltoanalytics.apps.analytics.views',
    url(r'^log/', 'log_pageview', name="analytics-log_pageview"),
    url(r'^test/', direct_to_template, {'template' : 'analytics/test.html' }, name="analytics-test"),
    url(r'^show/', 'show_raw_log', name="analytics-show"),
    url(r'^mobile/index/$', 'mobile_index', name="analytics-mobile_index"),
    url(r'^mobile/content/hot/$', 'mobile_hot_content', name="analytics-mobile_hot_content"),
    url(r'^mobile/content/mostviewed/$', 'mobile_most_viewed_content', name="analytics-mobile_most_viewed_content"),
    url(r'^mobile/users/activeperservice/$', 'mobile_active_users_per_service', name="analytics-mobile_active_users_per_service"),
)
