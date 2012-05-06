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
    
    # Read time in seconds, updated in save()
    total_read_time = models.IntegerField()
    
    # Needs a ton of new fields, like user/session id, os,
    # any other browser parameter we are interested in..
    screen_width = models.IntegerField(verbose_name="Leveys")
    screen_height = models.IntegerField(verbose_name="Korkeus")
    
    browser_name = models.CharField(max_length=16)
    browser_version = models.CharField(max_length=16)
    operating_system = models.CharField(max_length=16)

    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    referrer = models.CharField(max_length=255)
    
    def save(self, *args, **kwargs):
        difference = self.last_read_datetime - self.datetime
        self.total_read_time = difference.seconds
        super(Pageview, self).save(*args, **kwargs)
   

admin.site.register(Pageview)