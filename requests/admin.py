from django.contrib import admin

from requests.models import Client, FeatureRequest

# Register your models here.
admin.site.register(Client)
admin.site.register(FeatureRequest)
