from pickle import FALSE
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from . import serializers

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]
    return Response(routes)#safe = false mean we can use pthon dictionary inside json response
    
@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = serializers.RoomSerializer(rooms, many=True)#many true mean we are serializing many objects
    return Response(serializer.data)
    
@api_view(['GET'])
def getRoom(request,pk):
    room = Room.objects.get(id=pk)
    serializer = serializers.RoomSerializer(room, many=False)#many true mean we are serializing many objects
    return Response(serializer.data)
    