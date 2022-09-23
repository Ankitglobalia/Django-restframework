


from. models import Student
from.Serilizer import StudentSerilizer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
# Create your views here.
def Student_Detail(request,pk):
    st= Student.objects.get(id=pk)
    Serilizer=StudentSerilizer(st)
    json_Data=JSONRenderer().render(Serilizer.data)
    return HttpResponse(json_Data,content_type='application/json')


def Student_list(request):
    st= Student.objects.all()
    Serilizer=StudentSerilizer(st,many=True)
    json_Data=JSONRenderer().render(Serilizer.data)
    return HttpResponse(json_Data,content_type='application/json')






