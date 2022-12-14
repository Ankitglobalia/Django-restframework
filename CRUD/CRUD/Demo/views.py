



from functools import partial
import io
from requests import request
from rest_framework .parsers import JSONParser

from .models import Student
from.serializers import Studentserializer
from rest_framework .renderers import JSONRenderer
from django .http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def Student_Api(request):                       
    if request.method =='GET':
        json_data=request.body
        stream=io.BytesIO(json_data)

        pythondata= JSONParser().parse(stream) 

        id = pythondata.get('id', None)
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=Studentserializer(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')


        stu= Student.objects.all()
        serializer= Studentserializer(stu,many=True)   
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    if request.method =='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=Studentserializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()

            reg={'msg':' data created'}
            json_data=JSONRenderer().render(reg)
            return HttpResponse(json_data,content_type='application/json')  
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')    


    if request.method =='PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=  pythondata.get('id')
        stu= Student.objects.get(id=id)
        print(stu.name,'=============')
        serializer=Studentserializer(stu,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            reg={'msg':'data update'}
            json_data=JSONRenderer().render(reg)
            return HttpResponse(json_data,content_type='application/json')  
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')  




    if request.method=='DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id= pythondata.get('id')
        stu= Student.objects.get(id=id)
        stu.delete()
        reg={'msg':'data Deleted'}
        json_data=JSONRenderer().render(reg)
        return HttpResponse(json_data,content_type='application/json')  

