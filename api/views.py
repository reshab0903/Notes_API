#from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note

@api_view(['GET'])
def getRoutes(request):
    routes=[
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes' 
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns an single note object' 
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Created new notes with post request' 
        },
         {
            'Endpoint': '/notes/id/update',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Upadte existing notes with PUT request' 
        },
        {
            'Endpoint': '/notes/id/delete',
            'method': 'DELETE',
            'body': None,
            'description': 'Delete existing notes with DELETE request' 
        },

    ]
    return Response(routes)
    #safe=False means we can convert and data to Jsonresponse

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request,pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createNote(request):
    data = request.data
    note = Note.objects.create(
        body=data['body']
        )
    serializer = NoteSerializer(note,many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteNote(request,pk):
    note=Note.objects.get(id=pk)
    note.delete()
    return Response("Note was Deleted")

@api_view(['PUT'])
def updateNote(request,pk):
    data = request.data
    print('h1',data)
    note=Note.objects.get(id=pk)
    print('h2',note)
     
    serializer = NoteSerializer(note,data=request.data)
    print('h3',data)
    print('h4',serializer)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

