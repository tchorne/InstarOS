from json import JSONEncoder
import json
from django.shortcuts import render
from .models import Planet,Star

def map(request):
    star_list = Star.objects.all()
    planet_list = Planet.objects.all()

    context = {
        'star_list': star_list,
        'planet_list': planet_list,
    }
    return render(request,'map/map.html',context)