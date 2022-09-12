from django.shortcuts import render
from.models import Student
from.Serializers import Studentserilizer
from rest_framework import viewsets
from rest_framework .authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class StudentModelview(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=Studentserilizer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    