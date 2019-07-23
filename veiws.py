from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Officer
from .models import OfficerSerializers
class Officer(APIView):
    def get(self,request):
        employees1=employees.objects.all()
        serializer=employees.Serializer(employees1,many=True)
    def post(self):
        pass
    