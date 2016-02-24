from django.conf.urls import url

from views import dash

urlpatterns = [
    url(r'^$', dash.all_requests, name='home'),
]