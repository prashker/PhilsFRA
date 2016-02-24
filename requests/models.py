from __future__ import unicode_literals

from django.db import models
import datetime


class Client(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class FeatureRequest(models.Model):

    PRODUCT_AREAS = (
        ('P', 'Policies'),
        ('B', 'Billing'),
        ('C', 'Claims'),
        ('R', 'Reports')
    )

    title = models.CharField(max_length=50)
    description = models.TextField()
    client = models.ForeignKey(Client)
    priority = models.BigIntegerField()
    target_date = models.DateField(default=datetime.date.today)
    ticket_url = models.URLField()
