# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 05:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='featurerequest',
            name='product_area',
            field=models.CharField(choices=[('U', 'Unassigned'), ('P', 'Policies'), ('B', 'Billing'), ('C', 'Claims'), ('R', 'Reports')], default='U', max_length=3),
        ),
    ]
