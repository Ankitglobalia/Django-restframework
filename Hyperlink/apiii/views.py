from django.shortcuts import render
from .models import Student
from.serializers import studentserializer
from rest_framework import viewsets
# Create your views here.


class studentModelview(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=studentserializer