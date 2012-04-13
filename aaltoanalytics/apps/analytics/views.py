# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Count

from .models import Pageview, Service
import datetime
import urllib

# Name says it all :-)
TRANSPARENT_1_PIXEL_GIF = "\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\xff\xff\xff\x00\x00\x00\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b"

def log_pageview(request):
    try:
        service = Service.objects.get(tracking_id=request.GET.get("tid"))
    except Service.DoesNotExist:
        raise
        #return HttpResponse(TRANSPARENT_1_PIXEL_GIF, content_type='image/gif') 

    params = { 'service' : service }
    # parse all parameters 
    params['screen_width'] = request.GET.get("screen_width", "0")
    params['screen_height'] = request.GET.get("screen_height", "0")
    params['url'] = request.GET.get("url", "")
    params['title'] = request.GET.get("title", "")
    params['user_id'] = request.GET.get('uid', '')

    params['referrer'] = request.GET.get("referrer", "")

    #for key, value in params.items():
    #    print key, " = ", urllib.unquote(value)

    params['datetime'] = datetime.datetime.utcnow()
    Pageview.objects.create(**params)

    # save pageview to database
    return HttpResponse(TRANSPARENT_1_PIXEL_GIF, content_type='image/gif') 

def show_raw_log(request):
    return render(request, 'analytics/show.html', {'pageviews' : Pageview.objects.all() })

def mobile_index(request):
    return render(request, 'analytics/mobile/index.html')

def mobile_hot_content(request):
    service_pageview_list = []
    for service in Service.objects.all():
        service_pageview_list.append({'service' : service, 'pageviews' : Pageview.objects.filter(service=service).values('url', 'title').annotate(Count("url")).order_by("-url__count")})
    return render(request, 'analytics/mobile/hot_content.html', {'service_pageview_list' : service_pageview_list })

def mobile_most_viewed_content(request):
    service_pageview_list = []
    for service in Service.objects.all():
        service_pageview_list.append({'service' : service, 'pageviews' : Pageview.objects.filter(service=service).values('url', 'title').annotate(Count("url")).order_by("-url__count")})
    return render(request, 'analytics/mobile/most_viewed_content.html', {'service_pageview_list' : service_pageview_list })
