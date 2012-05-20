# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.db.models import Count, Avg

from .models import Pageview, Service
import datetime
import urllib
from django.utils import simplejson as json

def log_pageview(request):
    """
    The workhorse for logging a new pageview to database.

    This view parses all GET-parameters that were passed in, saves
    a new pageview to database and returns JSONP-object that
    is used to update the pageview id to client side. This way
    read time can be updated easily for the same pageview using
    the given id.
    """
    try:
        service = Service.objects.get(tracking_id=request.GET.get("tid"))
    except Service.DoesNotExist:
        return HttpResponseNotFound("This service is not configured.")

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

    params['datetime'] = datetime.datetime.utcnow()
    params['last_read_datetime'] = params['datetime']
    pageview = Pageview.objects.create(**params)
    
    # return jsonp object
    return HttpResponse("AaltoAnalytics.setPageviewId("+str(pageview.id)+")", content_type='application/javascript') 
    
def update_last_read_time(request, pageview_id):
    """
    Updates last read time for the pageview with pageview_id.
    """
    pg = Pageview.objects.get(id=pageview_id)
    pg.last_read_datetime = datetime.datetime.utcnow()
    pg.save()
    # Return empty javascript
    return HttpResponse("", content_type="application/javascript")
