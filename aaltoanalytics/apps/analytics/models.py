# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin

class Service(models.Model):
    """
    Service defines one web service in Aalto ecosystem.

    Each service has it's own tracking_id that must be
    used by giving it to AaltoAnalytics.setTrackingId in
    order to correctly match pageviews with service.
    """
    name = models.CharField(max_length=32)
    tracking_id = models.CharField(max_length=8)

admin.site.register(Service)

# Create your models here.
class Pageview(models.Model):
    """
    Pageview is the basic building block for user tracking.

    As user's browse the services in Aalto, pageviews are logged.
    These pageviews store everything that is needed to construct
    basically any query about the user ecosystem.
    """
    service = models.ForeignKey(Service)

    user_id = models.CharField(max_length=8)

    # The momemnt this pageview was issued
    datetime = models.DateTimeField()
    
    last_read_datetime = models.DateTimeField()
    # Needs a ton of new fields, like user/session id, os,
    # any other browser parameter we are interested in..
    screen_width = models.IntegerField(verbose_name="Leveys")
    screen_height = models.IntegerField(verbose_name="Korkeus")

    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    referrer = models.CharField(max_length=255)
