from django_hosts import patterns, host
from django.conf import settings

host_patterns = patterns('',
    host(r'analytics', 'aaltoanalytics.apps.analytics.urls', name='analytics'),
    host(r'www', settings.ROOT_URLCONF, name="normal")
)
