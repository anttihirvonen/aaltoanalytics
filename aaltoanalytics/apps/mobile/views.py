# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.db.models import Count, Avg

from aaltoanalytics.apps.analytics.models import Pageview, Service
import datetime
import urllib
from django.utils import simplejson as json

def active_time_limit(hours=1):
    return datetime.datetime.utcnow() - datetime.timedelta(hours=int(hours))

def mobile_index(request):
    # pick only users that have been active in past hour
    active_users = Pageview.objects.values('user_id').filter(datetime__gte=active_time_limit()).distinct().count()
    return render(request, 'analytics/mobile/index.html', {'active_users' : active_users })

def mobile_hot_content(request):
    service_pageview_list = []
    hours = request.GET.get('hours', 1)
    # TODO: formulate into one query
    for service in Service.objects.all():
        service_pageview_list.append({'service' : service, 'pageviews' : Pageview.objects.filter(service=service, datetime__gte=active_time_limit(hours)).values('url', 'title').annotate(Avg("total_read_time")).order_by("-total_read_time__avg")})
    return render(request, 'analytics/mobile/hot_content.html', {'service_pageview_list' : service_pageview_list })

def mobile_most_viewed_content(request):
    service_pageview_list = []
    hours = request.GET.get('hours', 1)
    # TODO: formulate into one query
    for service in Service.objects.all():
        service_pageview_list.append({'service' : service, 'pageviews' : Pageview.objects.filter(service=service, datetime__gte=active_time_limit(hours)).values('url', 'title').annotate(Count("url")).order_by("-url__count")})
    return render(request, 'analytics/mobile/most_viewed_content.html', {'service_pageview_list' : service_pageview_list })

def mobile_active_users_per_service(request):
    hours = request.GET.get('hours', 1)
    # TODO: formulate into one query
    services = Service.objects.all()
    
    for service in services:
        service.users = Pageview.objects.values('user_id').filter(service=service, datetime__gte=active_time_limit(hours)).distinct().count()

    return render(request, 'analytics/mobile/active_users_per_service.html', {'services' : services})

def developer_view(request):
    pass
