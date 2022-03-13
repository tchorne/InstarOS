from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.urls import reverse
from .models import Character, Note


def index(request):
    character_list = Character.objects.order_by('-name')[::-1]
    context = {
        'character_list': character_list,
    }
    return render(request,'people/index.html',context)

def detail(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    notes_list = Note.objects.filter(character=character)
    return render(request, 'people/detail.html', {'character':character, 'notes_list':notes_list})

def submitNote(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    new_note = Note(character = character, note_text = request.POST['note'])
    new_note.save()
    return HttpResponseRedirect(reverse('people:detail', args=(character_id,)))