from django.http import HttpResponse
import io
from rest_framework .parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer

from django.views.decorators.csrf import csrf_exempt




# Create your views here.
@csrf_exempt
def Student_create(request):
    if request.method == 'POST':
        json_data=request.body

        stream=io.BytesIO(json_data)

        pythondata= JSONParser().parse(stream)         
        serializer= StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
              
            res={'msg':'Data Created!!!'}
            json_Data=JSONRenderer().render(res)
            return HttpResponse(json_Data,content_type='application/json')

        json_Data= JSONRenderer().render(serializer.errors)
        return HttpResponse(json_Data,content_type='application/json')






