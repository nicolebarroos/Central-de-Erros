from rest_framework import serializers
from erros.models import Erros
from contas.models import User

class ErrosModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Erros
        fields = ['id', 'level', 'decricao', 'data_hora', 'eventos']

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'username']