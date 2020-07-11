from django.db import models
from datetime import datetime

class Erros(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    level = models.CharField(max_length=50)
    decricao = models.CharField(max_length=100)
    data_hora = models.DateTimeField(default=datetime.now)
    eventos = models.CharField(max_length=50)

