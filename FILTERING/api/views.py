from django.shortcuts import render

from rest_framework.generics import ListAPIView
from.models import Student
from. Serializers import StudentSerializers
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class StudentApi(ListAPIView):
    queryset=Student.objects.all()
    # queryset=Student.objects.filter(passby='user1')
    # queryset=Student.objects.filter(passby='user2')
    serializer_class=StudentSerializers
    # CURENT USER ADMIN DATA CHECK
    # def get_queryset(self):
    #     user=self.request.user
    #     return Student.objects.filter(passby=user)
    filter_backends=[DjangoFilterBackend]
    # filterset_fields=['city']
    filterset_fields=['name','city']

        