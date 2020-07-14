from rest_framework import serializers
from erros.models import Erros
from contas.models import User

class ErrosModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Erros
        fields = ['id', 'level', 'descricao', 'origem', 'eventos', 'categoria']

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'username']