from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from rest_api.serializers import ErrosModelSerializer, UserModelSerializer
from rest_framework.authentication import TokenAuthentication
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from erros.models import Erros
from contas.models import User

class ErrosApiViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
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
    filterset_fields = ['categoria']
#http://localhost:8000/api/categorias/?categoria=Desenvolvimento
#http://localhost:8000/api/categorias/?categoria=Produção

class ErrosOrderList(generics.ListAPIView):
    queryset = Erros.objects.all()
    serializer_class = ErrosModelSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['level', 'eventos']
#http://localhost:8000/api/ordenar/?ordering=eventos
#http://localhost:8000/api/ordenar/?ordering=level

class ErrosShearch(generics.ListAPIView):
    queryset = Erros.objects.all()
    serializer_class = ErrosModelSerializer
    filter_backends = [SearchFilter]
    search_fields = ['level', 'origem']
#http://localhost:8000/api/buscar/?search=Error
#http://localhost:8000/api/buscar/?search=2020-07-15


class ArquivadosList(generics.ListAPIView):
    queryset = Erros.objects.all()
    serializer_class = ErrosModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['arquivar']
    
#http://localhost:8000/api/arquivados?arquivar=True