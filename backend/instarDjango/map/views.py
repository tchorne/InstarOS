from json import JSONEncoder
import json
from django.shortcuts import render
from .models import Body

def map(request):
    body_list = Body.objects.all()

    context = {
        'body_list': body_list,
        
    }
    return render(request,'map/map.html',context)