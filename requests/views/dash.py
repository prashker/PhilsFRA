from django.http import HttpResponse
from django.shortcuts import render


def all_requests(request):
    return render(request, 'dash.html')