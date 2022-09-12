from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .Serializers import StudentSerializer
from rest_framework .authentication import SessionAuthentication
from rest_framework .permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
# Create your views here.
class StudentModelviewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    # basic authentication
    # authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAuthenticated]

    authentication_classes=[SessionAuthentication]
    # permission_classes=[IsAuthenticated]
    # permission_classes=[IsAdminUser]  
    # permission_classes=[IsAuthenticatedOrReadOnly]
    # permission_classes=[DjangoModelPermissions]
    permission_classes=[DjangoModelPermissionsOrAnonReadOnly]