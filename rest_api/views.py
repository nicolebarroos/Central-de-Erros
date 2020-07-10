from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_api.serializers import ErrosModelSerializer, UserModelSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from erros.models import Erros
from contas.models import User

class ErrosApiViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Erros.objects.all()
    serializer_class = ErrosModelSerializer

class UserApiViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

