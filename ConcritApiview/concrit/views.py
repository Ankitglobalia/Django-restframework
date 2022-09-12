from django.shortcuts import render
from .models import Student
from.Serilizers import Studentserilizer
from rest_framework.generics import ListAPIView ,CreateAPIView ,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.
class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=Studentserilizer

class StudentCreate(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=Studentserilizer

class StudentRetrive(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=Studentserilizer

class StudentUpdate(UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=Studentserilizer    


class StudentDelete(DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=Studentserilizer 


class StudentListCreate(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=Studentserilizer     



class RetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=Studentserilizer   

class RetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=Studentserilizer   

class RUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=Studentserilizer   

