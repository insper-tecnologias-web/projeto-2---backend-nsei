from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Note
from .serializers import NoteSerializer

@api_view(['GET', 'POST'])
def api_note(request):

    if request.method == 'POST':
        filme = request.data
        print(filme)
        note = Note()
        note.title = filme['title']
        note.img = filme['children']['primaryImage']['url']
        note.ano = filme['children']['releaseDate']['year']

        note.save()
    all_notes = Note.objects.all()
    serialized_notes = NoteSerializer(all_notes, many=True)
    return Response(serialized_notes.data)