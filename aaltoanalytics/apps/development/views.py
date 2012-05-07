# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from aaltoanalytics.apps.analytics.models import Pageview
from django.db.models import Count, Avg
from datetime import datetime, timedelta

def development_index(request):
    start_date = request.GET.get("start_date", "")
    start_date = datetime.strptime(start_date, "%d%m%y") if start_date else datetime.utcnow() - timedelta(days=7)
 
    end_date = request.GET.get("end_date", "")
    end_date = datetime.strptime(end_date, "%d%m%y") if end_date else datetime.utcnow()
    
    # Since sqlite doesn't seem to support distinct in certain cases, this is a hack
    # -- works as a quick hack, but better solution needed..
    browsers = Pageview.objects.filter(datetime__gte=start_date, datetime__lte=end_date).values('browser_name').distinct()
    for b in browsers:
        b['user_count'] = Pageview.objects.filter(datetime__gte=start_date, datetime__lte=end_date, browser_name=b['browser_name']).values('user_id').distinct().count()
    return render(request, 'development/index.html', {'start_date' : start_date, 'end_date' : end_date, 'browsers' : browsers })
    
def development_show_raw_log(request):
    return render(request, 'analytics/show.html', {'pageviews' : Pageview.objects.all() })
