from django.db import models
from datetime import datetime

STATUS_CHOICES = [
    ('Produção', 'Produção'),
    ('Homologação', 'Homologação'),
    ('Desenvolvimento', 'Desenvolvimento')
]

class Categoria(models.Model):
    status = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.status

class Erros(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    level = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150)
    origem = models.DateTimeField(default=datetime.now)
    eventos = models.CharField(max_length=50)
    categoria = models.CharField('Categoria', max_length=50, choices=STATUS_CHOICES)
    arquivar = models.BooleanField(default=False)

    def __str__(self):
        return self.level

    class Meta:
        verbose_name = 'Erro'
        verbose_name_plural = 'Erros'
