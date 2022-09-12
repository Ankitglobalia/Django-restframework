from django import views
from django.shortcuts import render
from .models import Singer,Song
from .serializers import SingerSerializers,SongSerializers
from rest_framework import viewsets


# Create your views here.

class singerviewset(viewsets.ModelViewSet):
    queryset=Singer.objects.all()
    serializer_class=SingerSerializers



class songviewset(viewsets.ModelViewSet):
    queryset=Song.objects.all()
    serializer_class=SongSerializers
