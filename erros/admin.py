from django.contrib import admin
from .models import Categoria
from .models import Erros

class ErrosAdmin(admin.ModelAdmin):
    
    list_display = ['level', 'eventos', 'descricao']
    #search_fields = ['level', 'categoria', 'eventos']
    list_filter = ['eventos', 'categoria', 'level']

class CategoriaAdmin(admin.ModelAdmin):

    list_display = ['status', 'descricao']
    #search_fields = ['level', 'categoria', 'eventos']
    #list_filter = ['eventos', 'categoria', 'level']


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Erros, ErrosAdmin)

