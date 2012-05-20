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
    """
    Helper function to get the earliest pageview time that
    should be included in the query results.
    """
    # TODO: this should be moved to model/manager-level
    return datetime.datetime.utcnow() - datetime.timedelta(hours=int(hours))

def mobile_index(request):
    """
    Index page for mobile site.
    """
    # pick only users that have been active in past hour
    active_users = Pageview.objects.values('user_id').filter(datetime__gte=active_time_limit()).distinct().count()
    return render(request, 'mobile/index.html', {'active_users' : active_users })

def mobile_hot_content(request):
    """
    Renders the hot content mobile page.

    Hot content is the content that has been read the most.
    Currently the sorting is based on the average time on page,
    but as view counts should also matter, this should be
    actually calculated from weighted average of view counts
    and time on page.
    """
    service_pageview_list = []
    hours = request.GET.get('hours', 1)
    # TODO: formulate into one query and move to manager
    for service in Service.objects.all():
        service_pageview_list.append({'service' : service, 'pageviews' : Pageview.objects.filter(service=service, datetime__gte=active_time_limit(hours)).values('url', 'title').annotate(Avg("total_read_time")).order_by("-total_read_time__avg")})
    return render(request, 'mobile/hot_content.html', {'service_pageview_list' : service_pageview_list })

def mobile_most_viewed_content(request):
    """
    Renders the mobile page that shows the most viewed content,
    grouped by services.
    """
    service_pageview_list = []
    hours = request.GET.get('hours', 1)
    # TODO: formulate into one query and move to manager-level
    for service in Service.objects.all():
        service_pageview_list.append({'service' : service, 'pageviews' : Pageview.objects.filter(service=service, datetime__gte=active_time_limit(hours)).values('url', 'title').annotate(Count("url")).order_by("-url__count")})
    return render(request, 'mobile/most_viewed_content.html', {'service_pageview_list' : service_pageview_list })

def mobile_active_users_per_service(request):
    """
    Renders the mobile page that show active users per service
    in given timeframe.
    """
    hours = request.GET.get('hours', 1)
    # TODO: formulate into one query
    services = Service.objects.all()
    
    for service in services:
        service.users = Pageview.objects.values('user_id').filter(service=service, datetime__gte=active_time_limit(hours)).distinct().count()

    return render(request, 'mobile/active_users_per_service.html', {'services' : services})
