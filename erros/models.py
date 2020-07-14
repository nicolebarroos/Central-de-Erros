from django.db import models
from datetime import datetime

class Categoria(models.Model):
    status = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)

class Erros(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    level = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    origem = models.DateTimeField(default=datetime.now)
    eventos = models.CharField(max_length=50)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
