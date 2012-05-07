# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.db.models import Count, Avg

from .models import Pageview, Service
import datetime
import urllib
from django.utils import simplejson as json

# Name says it all :-)
TRANSPARENT_1_PIXEL_GIF = "\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\xff\xff\xff\x00\x00\x00\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b"

def log_pageview(request):
    try:
        service = Service.objects.get(tracking_id=request.GET.get("tid"))
    except Service.DoesNotExist:
        return HttpResponseNotFound("This service is not configured.")
        #return HttpResponse(TRANSPARENT_1_PIXEL_GIF, content_type='image/gif') 

    params = { 'service' : service }
    # parse all parameters 
    params['screen_width'] = request.GET.get("screen_width", "0")
    params['screen_height'] = request.GET.get("screen_height", "0")
    
    params['browser_name'] = request.GET.get('browser_name', '')
    params['browser_version'] = request.GET.get('browser_version', '')
    params['operating_system'] = request.GET.get('operating_system', '')
    
    params['url'] = request.GET.get("url", "")
    params['title'] = request.GET.get("title", "")
    params['user_id'] = request.GET.get('uid', '')

    params['referrer'] = request.GET.get("referrer", "")

    #for key, value in params.items():
    #    print key, " = ", urllib.unquote(value)

    params['datetime'] = datetime.datetime.utcnow()
    params['last_read_datetime'] = params['datetime']
    pageview = Pageview.objects.create(**params)
    
    # return jsonp object
    return HttpResponse("AaltoAnalytics.setPageviewId("+str(pageview.id)+")", content_type='application/javascript') 
    
def update_last_read_time(request, pageview_id):
    pg = Pageview.objects.get(id=pageview_id)
    pg.last_read_datetime = datetime.datetime.utcnow()
    pg.save()
    
    return HttpResponse("", content_type="application/javascript")

def show_raw_log(request):
    return render(request, 'analytics/show.html', {'pageviews' : Pageview.objects.all() })

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
