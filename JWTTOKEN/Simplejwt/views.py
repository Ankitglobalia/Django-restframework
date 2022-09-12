from django.shortcuts import render
from.models import Student
from rest_framework import viewsets
from rest_framework .permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.
class StudentModelviewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    # authentication_classes=[JWTAuthentication]
    # permission_classes=[IsAuthenticated]