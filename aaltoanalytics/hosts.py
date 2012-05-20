from django_hosts import patterns, host
from django.conf import settings

# Definitions of subdomains. This routes requests using
# different root url configurations for each subdomain.
host_patterns = patterns('',
    host(r'm', 'aaltoanalytics.apps.mobile.urls', name='mobile'),
    host(r'dev', 'aaltoanalytics.apps.development.urls', name='development'),
    host(r'www', settings.ROOT_URLCONF, name="normal")
)
