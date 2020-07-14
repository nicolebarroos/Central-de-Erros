from django.contrib import admin
from .models import Categoria
from .models import Erros

#Melhorar isso futuramente

def status_producao(modeladmin, request, queryset):
    queryset.update(categoria='1')
status_producao.short_description = "Marcar para Produção"

def status_homologacao(modeladmin, request, queryset):
    queryset.update(categoria='2')
status_homologacao.short_description = "Marcar para Homologação"

def status_desenvolvimento(modeladmin, request, queryset):
    queryset.update(categoria='3')
status_desenvolvimento.short_description = "Marcar para Desenvolvimento"

def status_arquivado(modeladmin, request, queryset):
    queryset.update(categoria='4')
status_arquivado.short_description = "Marcar para Arquivar"


class ErrosAdmin(admin.ModelAdmin):

    list_display = ['level', 'eventos', 'descricao', 'categoria']
    #search_fields = ['level', 'categoria', 'eventos']
    list_filter = ['eventos', 'categoria', 'level']
    actions = [status_producao, status_homologacao, status_desenvolvimento, status_arquivado]

class CategoriaAdmin(admin.ModelAdmin):

    list_display = ['status', 'descricao']
    #search_fields = ['level', 'categoria', 'eventos']
    #list_filter = ['eventos', 'categoria', 'level']


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Erros, ErrosAdmin)

