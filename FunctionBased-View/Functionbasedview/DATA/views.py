from ast import Return
from rest_framework .decorators import api_view
from rest_framework.response import Response


# # Create your views here.
# @api_view()
# def hello_world(request):
#     return Response({'msg':'hello World'})


# Create your views here.
@api_view(['GET'])
def hello_world(request):
    return Response({'msg':'hello World'})

# @api_view(['POST'])
# def hello_world(request):
#     if request.method=='POST':
#         print(request.data)
#         return Response({'msg':'this is post method'})

@api_view(['POST','GET'])
def hello_world(request):

    if request.method=='GET':
        print(request.data)
        return Response({'msg':'this is Get method'})
    if request.method=='POST':
        print(request.data)
        return Response({'msg':'this is post method','data': request.data})