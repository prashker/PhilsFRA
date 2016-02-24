from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.forms import ModelForm

from requests.models import FeatureRequest


class RequestForm(ModelForm):
    class Meta:
        model = FeatureRequest
        fields = ['priority']

def all_requests(request):
    context = {}

    # There is little logic necessary in the display
    # We simply want all feature requests.
    # Todo: Order by priority?
    context['requests'] = FeatureRequest.objects.all()

    return render(request, 'dash.html', context)

def view_request(request, id):

    featurereq = get_object_or_404(FeatureRequest, pk=id)

    context = {}
    context['request'] = featurereq

    return render(request, 'view.html', context)