from rest_framework import serializers
from erros.models import Erros

class ErrosModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Erros
        fields = ['level', 'decricao', 'data_hora', 'eventos']