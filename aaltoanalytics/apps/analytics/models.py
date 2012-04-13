from django.db import models

# Create your models here.
class Pageview(models.Model):
    """
    Pageview is the basic building block for user tracking.

    As user's browse the services in Aalto, pageviews are logged.
    These pageviews store everything that is needed to construct
    basically any query about the user ecosystem.
    """
    tracking_id = models.CharField(max_length=8)

    user_id = models.CharField(max_length=8)

    datetime = models.DateTimeField()
    # Needs a ton of new fields, like user/session id, os,
    # any other browser parameter we are interested in..
    screen_width = models.IntegerField(verbose_name="Leveys")
    screen_height = models.IntegerField(verbose_name="Korkeus")

    url = models.CharField(max_length=255)
    referrer = models.CharField(max_length=255)
