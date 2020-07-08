from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_api.serializers import ErrosModelSerializer

from erros.models import Erros

class ErrosApiViewSet(viewsets.ModelViewSet):
    queryset = Erros.objects.all()
    serializer_class = ErrosModelSerializer
