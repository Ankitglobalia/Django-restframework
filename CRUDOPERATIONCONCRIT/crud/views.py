from django.shortcuts import render
from .models import Student
from.Serializers import StudentSerializaer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.


class StudentListCreate(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class= StudentSerializaer   





class RUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializaer 
