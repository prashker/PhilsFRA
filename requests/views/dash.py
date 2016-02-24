from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm, DateInput
from django.db.models import F

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
    context['requests'] = FeatureRequest.objects.all().order_by('priority')

    return render(request, 'dash.html', context)

def view_request(request, id):
    featurereq = get_object_or_404(FeatureRequest, pk=id)
    context = dict()

    prev_priority = featurereq.priority

    form = None
    updated = False

    if request.method == "POST":
        # Assume we are updating the record
        formvals = RequestForm(request.POST, instance=featurereq)
        if formvals.is_valid():
            result = formvals.save()
            updated = True
            form = formvals
            __update_all_other_requests(result)
    else:
        form = RequestForm(instance=featurereq)

    context['request'] = featurereq
    context['form'] = form
    context['updated'] = updated

    return render(request, 'view.html', context)

def create_request(request):
    context = dict()

    form = None
    updated = False

    if request.method == "POST":
        # Assume we are updating the record
        formvals = RequestForm(request.POST)
        if formvals.is_valid():
            result = formvals.save()
            __update_all_other_requests(result)
            return redirect('view', id=result.id)
    else:
        form = RequestForm()

    context['form'] = form

    return render(request, 'view.html', context)


def __update_all_other_requests(featurerequest_obj):
    # If there's two records with the same priority now,
    # shift the other and all other records with higher priority up
    second_record = FeatureRequest.objects.exclude(pk=featurerequest_obj.id).filter(client=featurerequest_obj.client,
                                                                                    priority=featurerequest_obj.priority)
    if second_record:
        FeatureRequest.objects.exclude(
                pk=featurerequest_obj.id
            ).filter(
                client=featurerequest_obj.client,
                priority__gte=featurerequest_obj.priority
            ).update(
                priority=F('priority')+1
            )

