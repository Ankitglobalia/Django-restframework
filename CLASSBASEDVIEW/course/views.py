from django.shortcuts import render
from rest_framework .response import Response
from rest_framework import status

from .Serlializers import Studentserializer
from .models import Student

# Create your views here.
class Stdent_Api(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=Studentserializer(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=Studentserializer(stu,many=True)
        return Response(serializer.data)    

    def post(self,request,format=None): 
        serializer=Studentserializer(data= request.data)   
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data posted'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk,format=None):
        id=pk
        stu=Student.objects.get(id=id)
        Serializer=Studentserializer(stu,data=request.data)
        if  Serializer.is_valid():
            Serializer.save()
            return Response({'msg':'Data Camplitly Update'},status=status.HTTP_201_CREATED)
        return Response (Serializer.errors,status=status.HTTP_400_BAD_REQUEST)   
    
    
    def patch(self,request,pk,format=None):
        id=pk
        stu=Student.objects.get(id=id)
        Serializer=Studentserializer(stu,data=request.data,partial=True)
        if  Serializer.is_valid():
            Serializer.save()
            return Response({'msg':'Data Camplitly Update'},status=status.HTTP_201_CREATED)
        return Response (Serializer.errors,status=status.HTTP_400_BAD_REQUEST)       

    def delete(self,request,pk,format=None):
        id=pk
        stu=Student.objects.get(id=id)
        
        stu.delete( )   
        return Response({'msg':'deeted data'}) 