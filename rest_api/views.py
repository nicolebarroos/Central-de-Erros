from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_api.serializers import ErrosModelSerializer, UserModelSerializer

from erros.models import Erros
from contas.models import User

class ErrosApiViewSet(viewsets.ModelViewSet):
    queryset = Erros.objects.all()
    serializer_class = ErrosModelSerializer

class UserApiViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

