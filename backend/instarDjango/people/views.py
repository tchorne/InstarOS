from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Character


def index(request):
    character_list = Character.objects.order_by('-name')
    template = loader.get_template('people/index.html')
    context = {
        'character_list': character_list,
    }
    return render(request,'people/index.html',context)

def detail(request, character_id):
    response = "You're looking at the details of character %s."
    return HttpResponse(response % character_id) 

