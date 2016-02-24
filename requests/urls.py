from django.conf.urls import url

from views import dash

urlpatterns = [
    url(r'^$', dash.all_requests, name='home'),
    url(r'^request/(?P<id>[0-9]+)/$', dash.view_request, name='view'),
    url(r'^request/new/', dash.create_request, name='create')
]