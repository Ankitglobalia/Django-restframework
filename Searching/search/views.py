from django.shortcuts import render
from .Serializer import StudentSerializers
from.models import Student
from rest_framework.generics import ListAPIView
# from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter

# Create your views here.
class studentapi(ListAPIView):
    queryset=Student.objects.all()
    serializer_class= StudentSerializers
    filter_backends=[OrderingFilter]
    # search_fields=['city']
    # search_fields=['name','city']
    ordering_fields=['name']
    
    
    
    
    