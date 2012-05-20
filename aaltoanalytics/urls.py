from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^analytics/', include('aaltoanalytics.apps.analytics.urls')),
    url(r'^mobile/', include('aaltoanalytics.apps.mobile.urls')),
    url(r'^development/', include('aaltoanalytics.apps.development.urls')),
)
