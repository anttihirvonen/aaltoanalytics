from django.conf.urls import patterns, include, url

urlpatterns = patterns('aaltoanalytics.apps.analytics.views',
    url(r'^log/', 'log_pageview', name="analytics-log_pageview"),
)
