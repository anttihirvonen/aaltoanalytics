from django_hosts import patterns, host
from django.conf import settings

host_patterns = patterns('',
    # Not really mobile views, but for testing..
    host(r'm', 'aaltoanalytics.apps.analytics.urls', name='mobile'),
    host(r'dev', 'aaltoanalytics.apps.analytics.urls', name='development'),
    host(r'www', settings.ROOT_URLCONF, name="normal")
)
