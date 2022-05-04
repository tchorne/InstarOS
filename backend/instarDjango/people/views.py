from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.urls import reverse
from .models import Character, Note, Campaign


def index(request):
    c=request.GET.get('c','1')
    campaign_list = Campaign.objects.all()
    character_list = Character.objects.filter(campaign=c).order_by('-name')[::-1]
    context = {
        'character_list': character_list,
        'campaign_list': campaign_list,
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

def deleteNote(request, note_id):
    if request.method == 'POST':

        note = get_object_or_404(Note, pk=note_id)
        character = note.character

        note.delete()
        return HttpResponse(status='200', content={"success": True})
    return HttpResponseRedirect(reverse('people:detail', args=(character.id,)))