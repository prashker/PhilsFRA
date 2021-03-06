# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 03:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.core.management import call_command


class Migration(migrations.Migration):

    def load_my_initial_data(self, o):
        call_command("loaddata", "initial_users.json")

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FeatureRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('priority', models.BigIntegerField()),
                ('target_date', models.DateField(default=datetime.date.today)),
                ('ticket_url', models.URLField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requests.Client')),
            ],
        ),
        migrations.RunPython(load_my_initial_data)
    ]
