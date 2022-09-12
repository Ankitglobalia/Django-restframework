from django.shortcuts import render
from .Serializer import Studentserializer
from.models import Student
from rest_framework .renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.

def Student_detail(request,pk):
    stu=Student.objects.get(id=pk)
    print('student', stu)
    serializer=Studentserializer(stu)
    print('serializer', serializer)
    print(serializer.data)
    json_data=JSONRenderer().render(serializer.data)
    print('json_data',json_data)
    return HttpResponse(json_data,content_type='application/json')



def Student_list(request):
    stu=Student.objects.all()
    print('student', stu)
    serializer=Studentserializer(stu, many=True)
    print('serializer', serializer)
    print(serializer.data)
    json_data=JSONRenderer().render(serializer.data)
    print('json_data',json_data)
    return HttpResponse(json_data,content_type='application/json')    