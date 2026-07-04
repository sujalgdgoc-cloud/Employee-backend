from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import EmployeeModel
from .serializers import EmpSerializers

class EmployeeView(generics.ListCreateAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmpSerializers

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmpSerializers
    lookup_field = 'pk'
    