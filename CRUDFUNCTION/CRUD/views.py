

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from.Serializers import StudentSerializer



# Create your views here.

@api_view(['GET','POST','PUT','DELETE'])
def Student_Api(request):
    if request.method == 'GET':
        id=request.data.get('id')
        if id is not None :
           stu= Student.objects.get('id')
           Serializer=StudentSerializer(stu)
           print(Serializer)
           return Response(Serializer.data)

        stu=Student.objects.all()
        Serializer=StudentSerializer(stu,many=True)
        return Response(Serializer.data)
   
    if request.method =='POST':
        Serializer=StudentSerializer(data=request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response({'msg':'data created'})
        return Response(Serializer.errors)  

    if request.method=='PUT':
        id=request.data.get('id')
        stu=Student.objects.get(pk=id)
        Serializer=StudentSerializer(stu,data=request.data,partial=True)
        if Serializer.is_valid():
           Serializer.save()
           return Response({'msg':'Data updatae'})
        return Response(Serializer.errors)   

    if request.method=='DELETE':
        id=request.data.get('id')
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'data Deleted'})
     


