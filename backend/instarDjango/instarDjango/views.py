from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render

def index(request):
    return render(request, "people/home.html", {})

