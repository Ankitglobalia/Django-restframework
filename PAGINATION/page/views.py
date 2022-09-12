from django.shortcuts import render
from.serializers import StudentSerializers
from.models import Student
from rest_framework .generics import ListAPIView
from.mypagination import cursorpagination
# Create your views here.
class StudentApi(ListAPIView):
    queryset= Student.objects.all()
    serializer_class=StudentSerializers
    pagination_class=cursorpagination

