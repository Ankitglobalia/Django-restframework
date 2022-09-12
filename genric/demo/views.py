
from django.shortcuts import render
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView

from .models import Student
from.Serilizers import StudentSerializer

# Create your views here.
#list creat methos withot pk
class LCStudentList(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
         #Retrive update and destroy method ....Pk required 
class RUDStudentRetrive(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def Delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    
