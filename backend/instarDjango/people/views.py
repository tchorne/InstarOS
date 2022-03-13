from tkinter.messagebox import QUESTION
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.template import loader
from django.shortcuts import render
from .models import Character


def index(request):
    character_list = Character.objects.order_by('-name')
    context = {
        'character_list': character_list,
    }
    return render(request,'people/index.html',context)

def detail(request, character_id):
    character = get_object_or_404(Character, pk=character_id)

    return render(request, 'people/detail.html', {'character':character})

