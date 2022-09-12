
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .Serializers import StudentSerializer
from rest_framework import status



# Create your views here.
@api_view(['GET','POST'])
def GetStudent_Api(request):
    if request.method == 'GET':
        # id=pk
        # if id is not None :
        #    stu= Student.objects.get('id').first()
        #    Serializer=StudentSerializer(stu)
        #    print(Serializer)
        #    return Response(Serializer.data)

        stu=Student.objects.all()
        Serializer=StudentSerializer(stu,many=True)
        return Response(Serializer.data)
   
    if request.method =='POST':
        Serializer=StudentSerializer(data=request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response({'msg':'data created'},status=status.HTTP_201_CREATED)
        return Response(Serializer.errors)  


@api_view(['GET','PUT','PATCH','DELETE'])
def Student_Api(request,pk=None):
    if request.method == 'GET':
        id=pk
        if id is not None :
           stu= Student.objects.get(id=id)
           Serializer=StudentSerializer(stu)
           print(Serializer)
           return Response(Serializer.data)

    if request.method=='PUT':
        id=pk
        stu=Student.objects.get(id=id)
        Serializer=StudentSerializer(stu,data=request.data)
        if Serializer.is_valid():
           Serializer.save()
           return Response({'msg':'Data camplitly updatae'})
        return Response(Serializer.errors)   



    if request.method=='PATCH':
        id=pk
        stu=Student.objects.get(id=id)
        Serializer=StudentSerializer(stu,data=request.data,partial=True)
        if Serializer.is_valid():
           Serializer.save()
           return Response({'msg':'Datapartially updatae'})
        return Response(Serializer.errors)   
    

    if request.method=='DELETE':
        id=pk
        stu=Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'data Deleted'})
     


