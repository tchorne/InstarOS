from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.urls import reverse
from .models import Event, Campaign


def index(request):
    event_list = Event.objects.order_by('-time')
    context = {
        'event_list': event_list,
    }
    return render(request,'history/index.html',context)

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id); 
    return render(request, 'history/detail.html', {'event':event})