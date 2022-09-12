


from. models import Student
from.Serilizer import StudentSerilizer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
# Create your views here.
# MODEL OBJECT SINGLE STUDENT dATA
def Student_Detail(request,pk):

    st= Student.objects.get(id=pk)
    # print('st:',st)

    Serilizer=StudentSerilizer(st)
    # print('serilizer', Serilizer)
    # print('Serilizer:',Serilizer.data)
    json_Data=JSONRenderer().render(Serilizer.data)
    # # print('json_data:',json_Data)
    return HttpResponse(json_Data,content_type='application/json')
    # return JsonResponse(Serilizer.data)

# Queyset 
def Student_list(request):

    st= Student.objects.all()
    # print('st:',st)

    Serilizer=StudentSerilizer(st,many=True)
    # print('serilizer', Serilizer)
    # print('Serilizer:',Serilizer.data)
    json_Data=JSONRenderer().render(Serilizer.data)
    # print('json_data:',json_Data)
    return HttpResponse(json_Data,content_type='application/json')
    # return JsonResponse(Serilizer.data,safe=False)



