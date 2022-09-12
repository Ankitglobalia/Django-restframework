
from django.shortcuts import render
from.models import Student
from .Serializers import Studentserializers
from rest_framework import viewsets
from rest_framework .permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from Title.jack import Jackthrottrate
# Create your views here.
class StudentModelviewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=Studentserializers
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    throttle_classes=[AnonRateThrottle,Jackthrottrate]
