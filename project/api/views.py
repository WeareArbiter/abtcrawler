from django.shortcuts import render
from django.views import View
from rest_framework import generics
from rest_framework.response import Response

from project.models import RequestForm
from project.api.serializers import RequestFormSerializer

class RequestFormAPIView(generics.ListCreateAPIView):
    queryset = RequestForm.objects.all()
    serializer_class = RequestFormSerializer
