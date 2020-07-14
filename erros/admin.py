from django.contrib import admin
from .models import Categoria
from .models import Erros

#class Erros(admin.ModelAdmin):
#    list_filter = ( 'categorias', )

admin.site.register(Categoria)
admin.site.register(Erros)

