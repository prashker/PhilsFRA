from __future__ import unicode_literals

from django.db import models
import datetime


class Client(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class FeatureRequest(models.Model):

    # Codes can be up to 3 letters (per product_area limit)
    PRODUCT_AREAS = (
        ('U', 'Unassigned'),
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
    product_area = models.CharField(default='U', choices=PRODUCT_AREAS, max_length=3)

    def __unicode__(self):
        return "Feature Request {}".format(self.id)