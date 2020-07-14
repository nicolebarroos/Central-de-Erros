from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from rest_api.serializers import ErrosModelSerializer, UserModelSerializer
from rest_framework.authentication import TokenAuthentication
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from erros.models import Erros
from contas.models import User

class ErrosApiViewSet(viewsets.ModelViewSet):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    queryset = Erros.objects.all()
    serializer_class = ErrosModelSerializer

class UserApiViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

class CategoriaList(generics.ListAPIView):
    queryset = Erros.objects.all()
    serializer_class = ErrosModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['erros__level']