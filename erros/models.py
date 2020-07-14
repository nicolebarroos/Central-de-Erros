from django.db import models
from datetime import datetime

STATUS_CHOICES = [
    ('1', 'Produção'),
    ('2', 'Homologação'),
    ('3', 'Desenvolvimento'),
    ('4', 'Arquivado'),
]

class Categoria(models.Model):
    status = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.status

class Erros(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    level = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    origem = models.DateTimeField(default=datetime.now)
    eventos = models.CharField(max_length=50)
    categoria = models.CharField('Categoria', max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.level
