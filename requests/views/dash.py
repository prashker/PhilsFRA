from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.forms import ModelForm, DateInput

from requests.models import FeatureRequest


class RequestForm(ModelForm):
    class Meta:
        model = FeatureRequest
        fields = ['title',
                  'description',
                  'client',
                  'priority',
                  'target_date',
                  'ticket_url',
                  'product_area']
        widgets = {
            'target_date':  DateInput(attrs={'class': 'datepicker'}),
        }

def all_requests(request):
    context = dict()

    # There is little logic necessary in the display
    # We simply want all feature requests.
    # Todo: Order by priority?
    context['requests'] = FeatureRequest.objects.all()

    return render(request, 'dash.html', context)

def view_request(request, id):
    featurereq = get_object_or_404(FeatureRequest, pk=id)
    context = dict()

    form = None
    updated = False

    if request.method == "POST":
        # Assume we are updating the record
        formvals = RequestForm(request.POST, instance=featurereq)
        if formvals.is_valid():
            formvals.save()
            updated = True
            form = formvals
    else:
        form = RequestForm(instance=featurereq)

    context['request'] = featurereq
    context['form'] = form
    context['updated'] = updated

    return render(request, 'view.html', context)
